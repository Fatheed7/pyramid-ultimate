# Generated by Django 4.1.4 on 2022-12-24 02:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0003_category_despaced"),
    ]

    operations = [
        migrations.AlterField(
            model_name="game",
            name="name",
            field=models.CharField(max_length=200),
        ),
    ]
