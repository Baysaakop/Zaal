# Generated by Django 2.1.2 on 2019-05-29 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0003_court_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='city',
        ),
        migrations.RemoveField(
            model_name='address',
            name='district',
        ),
        migrations.RemoveField(
            model_name='address',
            name='section',
        ),
        migrations.RemoveField(
            model_name='address',
            name='street',
        ),
        migrations.RemoveField(
            model_name='section',
            name='city',
        ),
        migrations.RemoveField(
            model_name='section',
            name='district',
        ),
        migrations.RemoveField(
            model_name='street',
            name='city',
        ),
        migrations.RemoveField(
            model_name='street',
            name='district',
        ),
        migrations.RemoveField(
            model_name='street',
            name='section',
        ),
        migrations.RemoveField(
            model_name='court',
            name='address',
        ),
        migrations.AddField(
            model_name='court',
            name='city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courts.City'),
        ),
        migrations.AddField(
            model_name='court',
            name='district',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courts.District'),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Section',
        ),
        migrations.DeleteModel(
            name='Street',
        ),
    ]
