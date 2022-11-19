from celery import shared_task

import requests

from store.models import Author, Book, Category, Publisher


@shared_task()
def data_synchronization():
    url = 'http://book-warehouse:8001/api/v1/book/'
    data_warehouse = requests.get(url)

    if data_warehouse.status_code != 200:
        raise ConnectionError('!!!!!!!!!!!_____no conect!')
    for item in data_warehouse.json():
        author, create_aut = Author.objects.update_or_create(name=item['author'])

        publisher, create_pub = Publisher.objects.update_or_create(name=item['publisher'])

        category, create_cat = Category.objects.update_or_create(name=item['category'])

        book, create_book = Book.objects.update_or_create(name=item['name'],
                                                          code=item['code'],
                                                          publisher=publisher,
                                                          category=category,
                                                          quantity_str=item['quantity_str'],
                                                          year=item['year'],
                                                          language=item['language'],
                                                          image=item['image'],
                                                          price=item['price'],
                                                          description=item['description'])
        book.author.add(author.id)
    return data_warehouse.status_code
