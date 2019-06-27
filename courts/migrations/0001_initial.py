# Generated by Django 2.1.2 on 2019-05-23 06:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Court',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('phone_number', models.CharField(max_length=8)),
                ('address', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='courts.Address')),
            ],
        ),
        migrations.CreateModel(
            name='CourtImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='img/courts/sample.png', upload_to='img/courts/')),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='courts.Court')),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courts.City')),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courts.City')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courts.District')),
            ],
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courts.City')),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courts.District')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courts.Section')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courts.City'),
        ),
        migrations.AddField(
            model_name='address',
            name='district',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courts.District'),
        ),
        migrations.AddField(
            model_name='address',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courts.Section'),
        ),
        migrations.AddField(
            model_name='address',
            name='street',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courts.Street'),
        ),
    ]
