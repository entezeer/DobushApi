# Generated by Django 2.2.14 on 2020-11-12 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20201112_1909'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='source',
            name='poll',
        ),
        migrations.AddField(
            model_name='news',
            name='poll',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Poll'),
        ),
    ]
