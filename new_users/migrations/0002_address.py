# Generated by Django 2.2 on 2020-03-03 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('new_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_name', models.CharField(max_length=30)),
                ('street_name', models.CharField(max_length=30)),
                ('locality', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('pincode', models.DecimalField(decimal_places=2, max_digits=6)),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='new_users.UserProfile')),
            ],
        ),
    ]
