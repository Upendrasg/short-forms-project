# Generated by Django 2.2.10 on 2021-09-23 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verified', models.BooleanField()),
                ('roof_material', models.CharField(choices=[('PQ', 'Poor Quality'), ('GQ', 'Good Quality'), ('BQ', 'Best Quality')], default='GQ', max_length=2)),
                ('house_age', models.CharField(choices=[('1Y', 'Less than 1 year'), ('2Y', 'Between 1 - 5 years'), ('5Y', 'More than 5 years')], default='2Y', max_length=2)),
                ('internal_switchboard', models.BooleanField()),
                ('switchboard_photo_afar', models.BinaryField()),
                ('switchboard_photo_enclosure', models.BinaryField()),
                ('switchboard_photo_upclose', models.BinaryField()),
            ],
            options={
                'verbose_name_plural': 'Property',
            },
        ),
    ]
