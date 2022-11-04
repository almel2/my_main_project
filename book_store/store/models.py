from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    name = models.CharField(_('name'), max_length=150, null=True)

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')

    def __str__(self):
        return f'Author - {self.name}'


class Publisher(models.Model):
    name = models.CharField(max_length=150)

    class Meta:
        verbose_name = _('Publisher')
        verbose_name_plural = _('Publishers')

    def __str__(self):
        return f'Publisher - {self.name}'


class Category(models.Model):
    name = models.CharField(_('name'), max_length=100)

    def __str__(self):
        return f'Category - {self.name}'


class Book(models.Model):
    name = models.CharField(_('name'), max_length=200)
    author = models.ManyToManyField('store.Author', verbose_name=_('author'))
    isbn = models.CharField(_('isbn'), max_length=50, null=True)
    code = models.IntegerField(_('code'))
    publisher = models.ForeignKey('store.Publisher', on_delete=models.CASCADE)
    category = models.ForeignKey('store.Category', verbose_name=_('category'), on_delete=models.PROTECT)
    str = models.CharField(_('str'), max_length=50, null=True)
    year = models.CharField(_('year'), max_length=50, null=True)
    language = models.CharField(_('language'), max_length=50)
    image = models.ImageField(_('image'))
    price = models.FloatField(_('price'))
    description = models.TextField(_('description'))

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    def __str__(self):
        return f'Book - {self.name[5:]}, price - {self.price}'
