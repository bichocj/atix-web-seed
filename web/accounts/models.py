from django.db import models
from django.utils.translation import ugettext as _


class Config(models.Model):
    class Meta:
        verbose_name = _('configuration')
        verbose_name_plural = _('configuration')

    can_anyone_register = models.BooleanField(default=False)

    def get():
    	return Config.objects.get_or_create(pk=1)[0]
