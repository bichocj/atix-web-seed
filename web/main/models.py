from django.db import models
from django.utils.translation import ugettext as _
from redactor.fields import RedactorField


class Category(models.Model):
    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')

    name = models.CharField(max_length=25)


class Post(models.Model):
    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')

    title = models.CharField(max_length=50, verbose_name=_('title'))
    content = RedactorField(verbose_name=_('content'))

    image = models.ImageField(null=True)
    publish_at = models.DateTimeField(verbose_name=_('publish date'))
    category = models.ForeignKey(Category, verbose_name=_('category'))

    def __str__(self):
        return  self.title
