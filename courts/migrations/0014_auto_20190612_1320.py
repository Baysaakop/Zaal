# Generated by Django 2.1.2 on 2019-06-12 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0013_auto_20190612_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='court',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
