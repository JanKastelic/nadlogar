# Generated by Django 3.2.6 on 2021-09-21 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("documents", "0003_auto_20210916_0852"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="document",
            options={"ordering": ["-date", "name"]},
        ),
    ]