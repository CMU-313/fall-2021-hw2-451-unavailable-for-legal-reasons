from django.utils.translation import ugettext_lazy as _
from mayan.apps.navigation.classes import Menu
from .icons import icon_menu_reviewers

menu_reviewers = Menu(
  icon=icon_menu_reviewers,
  label=_('Reviewers'),
  name='reviewers'
)
