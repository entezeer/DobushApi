# Generated by Django 2.2.14 on 2020-07-17 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200717_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='details_url',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
    ]
