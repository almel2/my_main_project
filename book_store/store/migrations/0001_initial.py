# Generated by Django 4.1.1 on 2022-10-12 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Publisher',
                'verbose_name_plural': 'Publishers',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('isbn', models.CharField(max_length=50, verbose_name='isbn')),
                ('code', models.IntegerField(verbose_name='code')),
                ('str', models.CharField(max_length=10, verbose_name='str')),
                ('year', models.CharField(max_length=10, verbose_name='year')),
                ('language', models.CharField(max_length=50, verbose_name='language')),
                ('image', models.ImageField(upload_to='', verbose_name='image')),
                ('price', models.FloatField(verbose_name='price')),
                ('description', models.TextField(verbose_name='description')),
                ('author', models.ManyToManyField(to='store.author', verbose_name='author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='store.category', verbose_name='category')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.publisher')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
    ]
