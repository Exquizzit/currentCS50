# Generated by Django 3.2.7 on 2021-09-18 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_listing'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='desc',
            field=models.CharField(default='No Description', max_length=100),
        ),
        migrations.AddField(
            model_name='listing',
            name='price',
            field=models.IntegerField(default=1),
        ),
    ]
