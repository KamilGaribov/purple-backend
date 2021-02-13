# Generated by Django 3.0.4 on 2021-02-11 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name_plural': 'Mektub'},
        ),
        migrations.AlterModelOptions(
            name='homepageproduct',
            options={'verbose_name': 'Ancaq 1-ci say işləyir', 'verbose_name_plural': 'Ana səhifə sayları'},
        ),
        migrations.AlterModelOptions(
            name='marsipan',
            options={'verbose_name_plural': 'Marsipan'},
        ),
        migrations.AlterModelOptions(
            name='marsipancategory',
            options={'verbose_name_plural': 'Marispan kateqoriyaları'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name_plural': 'Sifaris'},
        ),
        migrations.AlterModelOptions(
            name='vitrin',
            options={'verbose_name_plural': 'Vitrin'},
        ),
        migrations.AlterModelOptions(
            name='vitrincategory',
            options={'verbose_name_plural': 'Vitrin kateqoriyaları'},
        ),
        migrations.AlterModelOptions(
            name='xonca',
            options={'verbose_name_plural': 'Xonca'},
        ),
        migrations.AlterModelOptions(
            name='xoncacategory',
            options={'verbose_name_plural': 'Xonça kateqoriyaları'},
        ),
        migrations.RemoveField(
            model_name='flower',
            name='weight',
        ),
        migrations.RemoveField(
            model_name='xonca',
            name='weight',
        ),
        migrations.AlterField(
            model_name='flower',
            name='name',
            field=models.CharField(max_length=63, unique=True),
        ),
        migrations.AlterField(
            model_name='flowercategory',
            name='name',
            field=models.CharField(max_length=63, unique=True),
        ),
        migrations.AlterField(
            model_name='marsipan',
            name='name',
            field=models.CharField(max_length=63, unique=True),
        ),
        migrations.AlterField(
            model_name='marsipancategory',
            name='name',
            field=models.CharField(max_length=63, unique=True),
        ),
        migrations.AlterField(
            model_name='vitrin',
            name='name',
            field=models.CharField(max_length=63, unique=True),
        ),
        migrations.AlterField(
            model_name='vitrincategory',
            name='name',
            field=models.CharField(max_length=63, unique=True),
        ),
        migrations.AlterField(
            model_name='xonca',
            name='name',
            field=models.CharField(max_length=63, unique=True),
        ),
        migrations.AlterField(
            model_name='xoncacategory',
            name='name',
            field=models.CharField(max_length=63, unique=True),
        ),
    ]