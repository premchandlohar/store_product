# Generated by Django 2.2 on 2020-03-12 15:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trialapp', '0008_auto_20200312_1758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='followership',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='new_users.UserProfile'),
        ),
    ]
