# Generated by Django 2.0.7 on 2018-10-17 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a_player', '0003_torrentmodel_film'),
    ]

    operations = [
        migrations.AddField(
            model_name='torrentmodel',
            name='quality',
            field=models.DecimalField(choices=[(1, '720p'), (2, '1080p')], decimal_places=0, default=1, max_digits=1),
            preserve_default=False,
        ),
    ]
