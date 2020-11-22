import logging
import os

from django.apps import apps
from django.db import models, transaction
from django.urls import reverse
from django.utils.functional import cached_property
from django.utils.translation import ugettext_lazy as _

from mayan.apps.common.classes import ModelQueryFields
from mayan.apps.common.mixins import ModelInstanceExtraDataAPIViewMixin
from mayan.apps.events.classes import EventManagerMethodAfter, EventManagerSave
from mayan.apps.events.decorators import method_event
from mayan.apps.templating.classes import Template

from ..events import (
    event_document_version_created, event_document_version_deleted,
    event_document_version_edited
)
from ..literals import STORAGE_NAME_DOCUMENT_VERSION_PAGE_IMAGE_CACHE
from ..signals import signal_post_document_version_remap

from .document_models import Document

__all__ = ('DocumentVersion', 'DocumentVersionSearchResult')
logger = logging.getLogger(name=__name__)


class DocumentVersion(ModelInstanceExtraDataAPIViewMixin, models.Model):
    document = models.ForeignKey(
        on_delete=models.CASCADE, related_name='versions', to=Document,
        verbose_name=_('Document')
    )
    timestamp = models.DateTimeField(
        auto_now_add=True, db_index=True, help_text=_(
            'The server date and time when the document version was created.'
        ), verbose_name=_('Timestamp')
    )
    comment = models.TextField(
        blank=True, default='', help_text=_(
            'An optional short text describing the document version.'
        ), verbose_name=_('Comment')
    )
    active = models.BooleanField(
        default=True, help_text=_(
            'Determines the active version of the document.'
        ), verbose_name=_('Active')
    )

    class Meta:
        ordering = ('timestamp',)
        verbose_name = _('Document version')
        verbose_name_plural = _('Document versions')

    @staticmethod
    def annotate_content_object_list(content_object_list, start_page_number=None):
        def content_object_to_dictionary(entry):
            # Argument order based on the return value of enumerate
            return {
                'content_object': entry[1],
                'page_number': entry[0]
            }

        return map(
            content_object_to_dictionary, enumerate(
                iterable=content_object_list or (), start=start_page_number or 1
            )
        )

    def __str__(self):
        return self.get_label()

    def active_set(self, save=True):
        with transaction.atomic():
            self.document.versions.exclude(pk=self.pk).update(active=False)
            self.active = True

            if save:
                return self.save()

    @cached_property
    def cache(self):
        Cache = apps.get_model(app_label='file_caching', model_name='Cache')
        return Cache.objects.get(
            defined_storage_name=STORAGE_NAME_DOCUMENT_VERSION_PAGE_IMAGE_CACHE
        )

    @cached_property
    def cache_partition(self):
        partition, created = self.cache.partitions.get_or_create(
            name='version-{}'.format(self.uuid)
        )
        return partition

    @method_event(
        event_manager_class=EventManagerMethodAfter,
        event=event_document_version_deleted,
        target='document',
    )
    def delete(self, *args, **kwargs):
        for page in self.pages.all():
            page.delete()

        self.cache_partition.delete()

        return super().delete(*args, **kwargs)

    def export(self, file_object):
        first_page = self.pages.first()
        first_page.export(file_object=file_object)

        for page in self.pages[1:]:
            page.export(append=True, file_object=file_object)

    def get_absolute_url(self):
        return reverse(
            viewname='documents:document_version_preview', kwargs={
                'document_version_id': self.pk
            }
        )

    def get_api_image_url(self, *args, **kwargs):
        first_page = self.pages.first()
        if first_page:
            return first_page.get_api_image_url(*args, **kwargs)

    def get_label(self, preserve_extension=False):
        if preserve_extension:
            filename, extension = os.path.splitext(self.document.label)
            #return '{} ({}){}'.format(
            #    filename, self.get_rendered_timestamp(), extension
            #)
            return Template(
                template_string='{{ filename }} ({{ instance.timestamp }}){{ extension }}'
            ).render(
                context={
                    'extension': extension,
                    'filename': filename,
                    'instance': self
                }
            )
        else:
            return Template(
                template_string='{{ instance.document }} ({{ instance.timestamp }})'
            ).render(
                context={'instance': self}
            )
    get_label.short_description = _('Label')

    #def get_rendered_timestamp(self):
    #    return Template(
    #        template_string='{{ instance.timestamp }}'
    #    ).render(
    #        context={'instance': self}
    #    )

    @property
    def is_in_trash(self):
        return self.document.is_in_trash

    @property
    def page_count(self):
        """
        The number of pages that the document posses.
        """
        return self.pages.count()

    @property
    def page_content_objects(self):
        result = []
        for page in self.pages.all():
            result.append(page.content_object)

        return result

    @property
    def pages(self):
        DocumentVersionPage = apps.get_model(
            app_label='documents', model_name='DocumentVersionPage'
        )
        queryset = ModelQueryFields.get(model=DocumentVersionPage).get_queryset()
        return queryset.filter(pk__in=self.version_pages.all())

    def pages_remap(self, annotated_content_object_list=None):
        for page in self.pages.all():
            page.delete()

        if not annotated_content_object_list:
            annotated_content_object_list = ()

        for content_object_entry in annotated_content_object_list:
            self.version_pages.create(
                content_object=content_object_entry['content_object'],
                page_number=content_object_entry['page_number']
            )

        signal_post_document_version_remap.send(
            sender=DocumentVersion, instance=self
        )

    def pages_reset(self, document_file=None):
        """
        Remove all page mappings and recreate them to be a 1 to 1 match
        to the latest document file or the document file supplied.
        """
        latest_file = document_file or self.document.file_latest

        if latest_file:
            content_object_list = list(latest_file.pages.all())
        else:
            content_object_list = None

        annotated_content_object_list = DocumentVersion.annotate_content_object_list(
            content_object_list=content_object_list
        )
        return self.pages_remap(
            annotated_content_object_list=annotated_content_object_list
        )

    @method_event(
        event_manager_class=EventManagerSave,
        created={
            'event': event_document_version_created,
            'action_object': 'document',
            'target': 'self',
        },
        edited={
            'event': event_document_version_edited,
            'action_object': 'document',
            'target': 'self',
        }
    )
    def save(self, *args, **kwargs):
        with transaction.atomic():
            if self.active:
                self.active_set(save=False)

            return super().save(*args, **kwargs)

    @property
    def uuid(self):
        # Make cache UUID a mix of document UUID, file ID
        return '{}-{}'.format(self.document.uuid, self.pk)


class DocumentVersionSearchResult(DocumentVersion):
    class Meta:
        proxy = True
