# Generated by Django 4.0.10 on 2024-05-09 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_book_formats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.IntegerField(default=2004),
        ),
    ]
