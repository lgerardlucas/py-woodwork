# Generated by Django 3.2.4 on 2021-06-28 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomstype', '0002_alter_roomstype_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roomstype',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nome do Imóvel'),
        ),
    ]