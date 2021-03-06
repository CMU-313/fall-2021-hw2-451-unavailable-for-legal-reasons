from mayan.apps.documents.models import Document
from mayan.apps.documents.permissions import permission_document_create
from mayan.apps.documents.tests.base import GenericDocumentViewTestCase
from mayan.apps.sources.models import WebFormSource
from mayan.apps.sources.tests.literals import (
    TEST_SOURCE_LABEL, TEST_SOURCE_UNCOMPRESS_N
)
from mayan.apps.sources.wizards import DocumentCreateWizardStep

from ..wizard_steps import DocumentCreateWizardStepCabinets

from .mixins import CabinetDocumentUploadWizardStepTestMixin, CabinetTestMixin


class CabinetDocumentUploadTestCase(
    CabinetTestMixin, CabinetDocumentUploadWizardStepTestMixin,
    GenericDocumentViewTestCase
):
    auto_upload_test_document = False

    def setUp(self):
        super().setUp()
        self.test_source = WebFormSource.objects.create(
            enabled=True, label=TEST_SOURCE_LABEL,
            uncompress=TEST_SOURCE_UNCOMPRESS_N
        )

    def tearDown(self):
        super().tearDown()
        DocumentCreateWizardStep.reregister_all()

    def test_upload_interactive_view_with_access(self):
        self._create_test_cabinet()
        self._create_test_cabinet()
        self.grant_access(
            obj=self.test_document_type, permission=permission_document_create
        )
        response = self._request_upload_interactive_document_create_view()

        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            self.test_cabinets[0] in Document.objects.first().cabinets.all()
        )
        self.assertTrue(
            self.test_cabinets[1] in Document.objects.first().cabinets.all()
        )

    def test_upload_interactive_cabinet_selection_view_with_access(self):
        DocumentCreateWizardStep.deregister_all()
        DocumentCreateWizardStep.reregister(name=DocumentCreateWizardStepCabinets.name)

        self._create_test_cabinet()
        self.grant_access(
            permission=permission_document_create, obj=self.test_document_type

        )

        response = self._request_wizard_view()
        self.assertEqual(response.status_code, 200)
