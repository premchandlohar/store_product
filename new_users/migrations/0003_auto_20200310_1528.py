# Generated by Django 2.2 on 2020-03-10 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trialapp', '0002_auto_20200305_1426'),
        ('new_users', '0002_auto_20200309_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followed', to='trialapp.Store')),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foallow', to='new_users.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='userprofile',
            name='person',
            field=models.ManyToManyField(through='new_users.Relationship', to='trialapp.Store'),
        ),
    ]
