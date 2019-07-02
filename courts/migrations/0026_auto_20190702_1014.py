# Generated by Django 2.1.2 on 2019-07-02 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0025_auto_20190701_1014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='duration',
        ),
        migrations.AddField(
            model_name='order',
            name='end_time',
            field=models.CharField(default='09:00', max_length=5),
        ),
        migrations.AlterField(
            model_name='order',
            name='start_time',
            field=models.CharField(default='08:00', max_length=5),
        ),
    ]
