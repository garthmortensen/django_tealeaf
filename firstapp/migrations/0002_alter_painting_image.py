# Generated by Django 4.2.11 on 2024-05-19 12:29

from django.db import migrations, models
import firstapp.models


class Migration(migrations.Migration):

    dependencies = [
        ("firstapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="painting",
            name="image",
            field=models.ImageField(upload_to=firstapp.models.get_upload_path),
        ),
    ]
