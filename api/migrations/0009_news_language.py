# Generated by Django 2.2.14 on 2020-09-30 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_delete_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='language',
            field=models.CharField(default=None, max_length=250),
        ),
    ]
