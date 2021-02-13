# Generated by Django 3.0.4 on 2021-02-13 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20210213_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backlink',
            name='action',
            field=models.CharField(choices=[('from_facebook', 'from_facebook'), ('from_instagram', 'from_instagram'), ('from_oxu_az', 'from_oxu_az'), ('to_facebook', 'to_facebook'), ('to_instagram', 'to_instagram')], max_length=15),
        ),
    ]
