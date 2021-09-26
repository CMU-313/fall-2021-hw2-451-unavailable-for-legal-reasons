from django.utils.translation import ugettext_lazy as _

from mayan.apps.navigation.classes import Menu

menu_reviewers = Menu(
    label=_('Reviewers'),
    name='reviewers' 
)