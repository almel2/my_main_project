# Generated by Django 4.1.1 on 2022-10-14 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_alter_author_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=50, null=True, verbose_name='isbn'),
        ),
    ]
