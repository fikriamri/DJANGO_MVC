# Generated by Django 2.2.3 on 2019-07-22 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dokter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('no_telp', models.CharField(max_length=17)),
                ('bidang', models.CharField(max_length=255)),
                ('jadwal_praktik', models.DateField()),
            ],
        ),
    ]
