# Generated by Django 2.1.2 on 2019-06-28 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0019_auto_20190628_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetable',
            name='day',
            field=models.CharField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')], default='Mon', max_length=3),
        ),
    ]
