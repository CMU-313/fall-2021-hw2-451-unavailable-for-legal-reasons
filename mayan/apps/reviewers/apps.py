from django.apps import AppConfig
from mayan.apps.common.apps import MayanAppConfig


class ReviewersConfig(MayanAppConfig):
    app_namespace = 'reviewers'
    app_url = 'reviewers'
    name = 'mayan.apps.reviewers'
