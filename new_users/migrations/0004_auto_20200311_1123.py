# Generated by Django 2.2 on 2020-03-11 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_users', '0003_auto_20200310_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='person',
        ),
        migrations.DeleteModel(
            name='Relationship',
        ),
    ]
