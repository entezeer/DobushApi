# Generated by Django 2.2.14 on 2020-09-30 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_news_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='language',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
    ]