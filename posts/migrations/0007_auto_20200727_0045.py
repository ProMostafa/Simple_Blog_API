# Generated by Django 3.0.6 on 2020-07-26 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20200727_0029'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='anonymous',
            new_name='person',
        ),
    ]
