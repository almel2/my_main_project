from django.db import models
from django.utils.translation import gettext_lazy as _


class Book(models.Model):
    name = models.CharField(_('name'), max_length=200)
    author = models.CharField(_('author'), max_length=200, null=True)
    code = models.IntegerField(_('code'))
    publisher = models.CharField(_('publisher'), max_length=200, null=True)
    category = models.CharField(_('category'), max_length=100)
    quantity_str = models.CharField(_('str'), max_length=50, null=True, blank=True)
    year = models.CharField(_('year'), max_length=50, null=True, blank=True)
    language = models.CharField(_('language'), max_length=50)
    image = models.ImageField(_('image'))
    price = models.DecimalField(_('price'), max_digits=7, decimal_places=2)
    description = models.TextField(_('description'))
    quantity = models.PositiveIntegerField(_('quantity'), default=0)

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')

    def __str__(self):
        return f'Book - {self.name[5:]}, price - {self.price}'


class BookInstance(models.Model):
    book = models.ForeignKey('warehouse_api.Book', on_delete=models.CASCADE)
    isbn = models.CharField(_('barcode'), max_length=50)

    def save(self, *args, **kwargs):
        super(BookInstance, self).save(*args, **kwargs)
        self.book.quantity += 1
        self.book.save()


    def delete(self, *args, **kwargs):
        super(BookInstance, self).delete(*args, **kwargs)
        self.book.quantity -= 1
        self.book.save()

    def __str__(self):
        return f'Book id - {self.book.id}, isbn - {self.isbn}'
