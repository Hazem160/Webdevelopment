# Generated by Django 4.1.6 on 2023-02-28 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_remove_bidd_item_remove_user_in_watchlist_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bidd',
            name='message',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
