# Generated by Django 4.0.10 on 2024-05-09 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_alter_book_options_alter_book_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='formats',
            field=models.TextField(default='Paperback, eBook'),
        ),
    ]
