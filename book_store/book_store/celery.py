import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'book_store.settings')

app = Celery('book_store')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


# @app.task(bind=True)
# def debug_task(self):
#     for _ in range(100):
#         print(f'Request: {self.request!r}')
