from django.core.management.base import BaseCommand
import os.path

import json

from store.models import Book, Author, Publisher, Category

BASE = os.path.dirname(os.path.abspath(__file__))


class Command(BaseCommand):
    help = 'This command create data'

    def handle(self, *args, **options):
        try:
            with open(os.path.join(BASE, 'data_base.json')) as file:
                data = file.read()
        except FileNotFoundError:
            self.stdout.write(self.style.ERROR(f'No such file or directory'))

        counter = 0
        for item in json.loads(data):
            counter += 1
            if item['author'] is not None:
                Author.objects.update_or_create(name=item['author'].split(',')[0])
            else:
                Author(name=item['author']).save()
            author = Author.objects.last()
            print('Author save')

            Publisher.objects.update_or_create(name=item['publisher'])
            publisher = Publisher.objects.last()
            print('publisher save')

            Category.objects.update_or_create(name=item['catalog'])
            category = Category.objects.last()
            print('Category save')

            Book(name=item['name'],
                 isbn=item['isbn'],
                 code=item['code'],
                 publisher=publisher,
                 category=category,
                 str=item['str'],
                 year=item['year'],
                 language=item['language'],
                 image=item['image'],
                 price=item['price'],
                 description=item['description']
                 ).save()
            Book.objects.last().author.add(author.id)
            self.stdout.write(self.style.SUCCESS(f'Created data {counter}'))
        self.stdout.write(self.style.SUCCESS(f'Success create date!'))
# ./manage.py create_data
