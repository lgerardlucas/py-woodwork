# Generated by Django 3.2.4 on 2021-07-02 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nome do Móvel')),
            ],
            options={
                'verbose_name': 'Móvel',
                'verbose_name_plural': 'Móveis',
                'ordering': ['name'],
            },
        ),
    ]
