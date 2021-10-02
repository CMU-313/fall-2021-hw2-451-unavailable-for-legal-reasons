from django.utils.translation import ugettext_lazy as _
from mayan.apps.navigation.classes import Link
from .icons import icon_menu_reviewers

link_reviewers = Link(
    icon=icon_menu_reviewers,text=_('Candidates'), view='candidates:candidates'
)