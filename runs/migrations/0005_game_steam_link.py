# Generated by Django 4.1.4 on 2022-12-15 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("runs", "0004_primarychallenge_additional_info_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="steam_link",
            field=models.URLField(blank=True),
        ),
    ]
