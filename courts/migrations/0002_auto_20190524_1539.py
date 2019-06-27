# Generated by Django 2.1.2 on 2019-05-24 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='court',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='court',
            name='phone_number',
            field=models.CharField(max_length=8, unique=True),
        ),
    ]