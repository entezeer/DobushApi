# Generated by Django 2.2.14 on 2020-07-18 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200718_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='title',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
    ]
