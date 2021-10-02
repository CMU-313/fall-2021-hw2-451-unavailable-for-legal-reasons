from django.apps import AppConfig
from mayan.apps.common.apps import MayanAppConfig

from mayan.apps.common.menus import (
    menu_facet, menu_list_facet, menu_main, menu_object, menu_return,
    menu_secondary, menu_setup, menu_multi_item
)

from .reviewer_links import link_reviewers
from .menus import menu_reviewers

class ReviewersConfig(MayanAppConfig):
    app_namespace = 'reviewers'
    app_url = 'reviewers'
    name = 'mayan.apps.reviewers'

    menu_main.bind_links(links=(link_reviewers,), position=0)
