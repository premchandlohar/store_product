# Generated by Django 2.2 on 2020-02-27 07:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trialapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'Subcategory', 'verbose_name_plural': 'Subcategories'},
        ),
    ]
