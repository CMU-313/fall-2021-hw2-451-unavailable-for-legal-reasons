from django.utils.translation import ugettext_lazy as _

from mayan.apps.permissions import PermissionNamespace

namespace = PermissionNamespace(label=_('Cabinets'), name='reviewers')

# Translators: this refers to the permission that will allow users to add
# documents to reviewers.
permission_reviewer_add_candidate = namespace.add_permission(
    label=_('Add candidates to reviewers'), name='reviewer_add_candidates'
)
permission_reviewer_create = namespace.add_permission(
    label=_('Create reviewers'), name='reviewer_create'
)
permission_reviewer_delete = namespace.add_permission(
    label=_('Delete reviewers'), name='reviewer_delete'
)
permission_reviewer_edit = namespace.add_permission(
    label=_('Edit reviewers'), name='reviewer_edit'
)
permission_reviewer_remove_candidate = namespace.add_permission(
    label=_('Remove candidates from reviewers'), name='reviewer_remove_candidates'
)
permission_reviewer_view = namespace.add_permission(
    label=_('View reviewers'), name='reviewer_view'
)

