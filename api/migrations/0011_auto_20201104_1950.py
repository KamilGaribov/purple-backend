# Generated by Django 3.1.2 on 2020-11-04 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20201103_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='cake',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/vitrin'),
        ),
        migrations.AddField(
            model_name='marsipan',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='img/marsipan'),
        ),
    ]
