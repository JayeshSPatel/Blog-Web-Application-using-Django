# Generated by Django 4.2.5 on 2023-09-16 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0003_alter_message_text"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="room",
            options={"ordering": ["-update", "-created"]},
        ),
    ]
