# Generated by Django 2.2 on 2019-04-05 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0006_auto_20190405_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]