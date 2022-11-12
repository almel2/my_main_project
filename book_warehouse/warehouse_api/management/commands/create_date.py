import json
import os.path
import random

from django.core.management.base import BaseCommand

from warehouse_api.models import Book, BookInstance


BASE = os.path.dirname(os.path.abspath(__file__))


class Command(BaseCommand):
    help = 'This command create data'

    def handle(self, *args, **options):
        with open(os.path.join(BASE, 'data_base.json')) as file:
            data = file.read()

        num_end = 0

        for item in json.loads(data):

            book = Book(name=item['name'],
                        code=item['code'],
                        author=item['author'],
                        publisher=item['publisher'],
                        quantity_str=item['str'],
                        year=item['year'],
                        language=item['language'],
                        image=item['image'],
                        price=item['price'],
                        description=item['description'])
            book.save()
            print('Book create')

            for _ in range(random.randrange(10, 50, 10)):
                isbn = '1238-8188-5678-'
                num_end += 1
                isbn += str(num_end).rjust(4, '0')
                BookInstance(book=book, isbn=isbn).save()



        self.stdout.write(self.style.SUCCESS('Success create date!'))
# ./manage.py create_date
