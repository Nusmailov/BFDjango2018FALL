# Generated by Django 2.1.1 on 2018-10-04 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_author_bday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='bday',
        ),
    ]