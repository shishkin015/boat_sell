# Generated by Django 4.2.6 on 2023-10-29 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='boat',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='цена'),
        ),
    ]
