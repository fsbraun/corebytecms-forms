from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class FormConfig(AppConfig):
    name = 'cms_forms'
    verbose_name = _('Forms')
