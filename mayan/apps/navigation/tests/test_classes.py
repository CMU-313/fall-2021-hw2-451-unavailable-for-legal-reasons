from django.template import Context
from django.urls import reverse

from furl import furl

from mayan.apps.acls.classes import ModelPermission
from mayan.apps.permissions import Permission, PermissionNamespace
from mayan.apps.testing.literals import TEST_VIEW_NAME
from mayan.apps.testing.tests.base import GenericViewTestCase

from ..classes import Link, Menu, SourceColumn

from .literals import (
    TEST_PERMISSION_NAMESPACE_NAME, TEST_PERMISSION_NAMESPACE_TEXT,
    TEST_PERMISSION_NAME, TEST_PERMISSION_LABEL, TEST_LINK_TEXT,
    TEST_MENU_NAME, TEST_QUERYSTRING_ONE_KEY, TEST_QUERYSTRING_TWO_KEYS,
    TEST_SUBMENU_NAME, TEST_UNICODE_STRING, TEST_URL
)


class LinkClassTestCase(GenericViewTestCase):
    def setUp(self):
        super().setUp()

        self.test_object = self._test_case_group

        self.add_test_view(test_object=self.test_object)

        self.namespace = PermissionNamespace(
            label=TEST_PERMISSION_NAMESPACE_TEXT,
            name=TEST_PERMISSION_NAMESPACE_NAME
        )

        self.test_permission = self.namespace.add_permission(
            name=TEST_PERMISSION_NAME, label=TEST_PERMISSION_LABEL
        )

        ModelPermission.register(
            model=self.test_object._meta.model,
            permissions=(self.test_permission,)
        )

        self.link = Link(text=TEST_LINK_TEXT, view=TEST_VIEW_NAME)
        Permission.invalidate_cache()

    def test_link_resolve(self):
        response = self.get(viewname=TEST_VIEW_NAME)

        context = Context({'request': response.wsgi_request})

        resolved_link = self.link.resolve(context=context)
        self.assertEqual(
            resolved_link.url, reverse(viewname=TEST_VIEW_NAME)
        )

    def test_link_permission_resolve_no_permission(self):
        link = Link(
            permissions=(self.test_permission,), text=TEST_LINK_TEXT,
            view=TEST_VIEW_NAME
        )

        response = self.get(viewname=TEST_VIEW_NAME)
        response.context.update({'request': response.wsgi_request})

        context = Context(response.context)

        resolved_link = link.resolve(context=context)
        self.assertEqual(resolved_link, None)

    def test_link_permission_resolve_with_permission(self):
        link = Link(
            permissions=(self.test_permission,), text=TEST_LINK_TEXT,
            view=TEST_VIEW_NAME
        )

        self.grant_access(obj=self.test_object, permission=self.test_permission)

        response = self.get(viewname=TEST_VIEW_NAME)
        response.context.update({'request': response.wsgi_request})

        context = Context(response.context)

        resolved_link = link.resolve(context=context)
        self.assertEqual(resolved_link.url, reverse(viewname=TEST_VIEW_NAME))

    def test_link_permission_resolve_with_acl(self):
        # ACL is tested agains the resolved_object or just {{ object }} if not
        link = Link(
            permissions=(self.test_permission,), text=TEST_LINK_TEXT,
            view=TEST_VIEW_NAME
        )

        self.grant_access(obj=self.test_object, permission=self.test_permission)

        response = self.get(viewname=TEST_VIEW_NAME)
        response.context.update({'request': response.wsgi_request})

        context = Context(response.context)

        resolved_link = link.resolve(context=context)
        self.assertNotEqual(resolved_link, None)
        self.assertEqual(resolved_link.url, reverse(viewname=TEST_VIEW_NAME))

    def test_link_with_unicode_querystring_request(self):
        url = furl(reverse(TEST_VIEW_NAME))
        url.args['unicode_key'] = TEST_UNICODE_STRING

        self.link.keep_query = True
        response = self.get(path=url.url)

        context = Context({'request': response.wsgi_request})

        resolved_link = self.link.resolve(context=context)

        self.assertEqual(resolved_link.url, url.url)

    def test_link_with_querystring_preservation(self):
        previous_url = '{}?{}'.format(
            reverse(TEST_VIEW_NAME), TEST_QUERYSTRING_TWO_KEYS
        )
        self.link.keep_query = True
        self.link.url = TEST_URL
        self.link.view = None
        response = self.get(path=previous_url)

        context = Context({'request': response.wsgi_request})

        resolved_link = self.link.resolve(context=context)
        self.assertEqual(
            resolved_link.url,
            '{}?{}'.format(TEST_URL, TEST_QUERYSTRING_TWO_KEYS)
        )

    def test_link_with_querystring_preservation_with_key_removal(self):
        previous_url = '{}?{}'.format(
            reverse(TEST_VIEW_NAME), TEST_QUERYSTRING_TWO_KEYS
        )
        self.link.keep_query = True
        self.link.url = TEST_URL
        self.link.view = None
        self.link.remove_from_query = ['key2']
        response = self.get(path=previous_url)

        context = Context({'request': response.wsgi_request})

        resolved_link = self.link.resolve(context=context)
        self.assertEqual(
            resolved_link.url,
            '{}?{}'.format(TEST_URL, TEST_QUERYSTRING_ONE_KEY)
        )


class MenuClassTestCase(GenericViewTestCase):
    def setUp(self):
        super().setUp()

        self.test_object = self._test_case_group

        self.add_test_view(test_object=self.test_object)

        self.namespace = PermissionNamespace(
            TEST_PERMISSION_NAMESPACE_NAME, TEST_PERMISSION_NAMESPACE_TEXT
        )

        self.test_permission = self.namespace.add_permission(
            name=TEST_PERMISSION_NAME, label=TEST_PERMISSION_LABEL
        )

        self.menu = Menu(name=TEST_MENU_NAME)
        self.sub_menu = Menu(name=TEST_SUBMENU_NAME)
        self.link = Link(text=TEST_LINK_TEXT, view=TEST_VIEW_NAME)
        Permission.invalidate_cache()

    def tearDown(self):
        Menu.remove(name=TEST_MENU_NAME)
        Menu.remove(name=TEST_SUBMENU_NAME)
        super().tearDown()

    def test_null_source_link_unbinding(self):
        self.menu.bind_links(links=(self.link,))

        response = self.get(viewname=TEST_VIEW_NAME)
        context = Context({'request': response.wsgi_request})
        self.assertEqual(
            self.menu.resolve(context=context)[0]['links'][0].link, self.link
        )

        self.menu.unbind_links(links=(self.link,))

        self.assertEqual(self.menu.resolve(context=context), [])

    def test_null_source_submenu_unbinding(self):
        self.menu.bind_links(links=(self.sub_menu,))

        response = self.get(viewname=TEST_VIEW_NAME)
        context = Context({'request': response.wsgi_request})

        self.assertEqual(
            self.menu.resolve(context=context)[0]['links'], [self.sub_menu]
        )

        self.menu.unbind_links(links=(self.sub_menu,))

        self.assertEqual(self.menu.resolve(context=context), [])


class SourceColumnClassTestCase(GenericViewTestCase):
    def setUp(self):
        super().setUp()

        self._create_test_object()

    def test_get_for_source_for_model_proxies_no_columns(self):
        TestModelProxy = self._create_test_model(
            base_class=self.TestModel, options={'proxy': True}
        )

        test_model_proxy = TestModelProxy.objects.create()

        columns = SourceColumn.get_for_source(source=test_model_proxy)

        self.assertEqual(len(columns), 0)

    def test_get_for_source_for_model_proxies_with_columns(self):
        SourceColumn(
            attribute='__str__', source=self.TestModel
        )

        TestModelProxy = self._create_test_model(
            base_class=self.TestModel, options={'proxy': True}
        )

        test_model_proxy = TestModelProxy.objects.create()

        columns = SourceColumn.get_for_source(source=test_model_proxy)

        self.assertEqual(len(columns), 1)

    def test_get_for_source_for_model_proxies_and_exclude_with_columns(self):
        column = SourceColumn(
            attribute='__str__', source=self.TestModel
        )

        TestModelProxy = self._create_test_model(
            base_class=self.TestModel, options={'proxy': True}
        )

        column.add_exclude(source=TestModelProxy)

        test_model_proxy = TestModelProxy.objects.create()

        columns = SourceColumn.get_for_source(source=test_model_proxy)

        self.assertEqual(len(columns), 0)

    def test_get_for_source_for_querysets_no_columns(self):
        columns = SourceColumn.get_for_source(
            source=self.TestModel.objects.all()
        )

        self.assertEqual(len(columns), 0)

    def test_get_for_source_for_querysets_with_columns(self):
        SourceColumn(
            attribute='__str__', source=self.TestModel
        )

        columns = SourceColumn.get_for_source(
            source=self.TestModel.objects.all()
        )

        self.assertEqual(len(columns), 1)
