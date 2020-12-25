# Generated by Django 3.0.4 on 2020-12-22 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cafe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=31)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('subject', models.CharField(max_length=31)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FlowerCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='HomePageProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vitrin', models.IntegerField(default=2)),
                ('marsipan', models.IntegerField(default=2)),
                ('flower', models.IntegerField(default=2)),
                ('xonca', models.IntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='MarsipanCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('surname', models.CharField(max_length=63)),
                ('email', models.EmailField(max_length=63)),
                ('city', models.CharField(default='Baki', max_length=63)),
                ('address', models.CharField(max_length=63)),
                ('address2', models.CharField(blank=True, max_length=63, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('orderid', models.IntegerField(unique=True)),
                ('sessionid', models.CharField(max_length=127, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('pan', models.CharField(blank=True, max_length=32, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('approved', 'approved'), ('cancelled', 'cancelled')], default='pending', max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='VitrinCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='XoncaCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
            ],
        ),
        migrations.CreateModel(
            name='Xonca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=12.0, max_digits=6, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('ingredient', models.CharField(blank=True, max_length=511, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('publish', models.BooleanField(default=True)),
                ('homepage', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, default=4, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.XoncaCategory')),
                ('similar1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='similar1_of', to='api.Xonca')),
                ('similar2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='similar2_of', to='api.Xonca')),
                ('similar3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='similar3_of', to='api.Xonca')),
                ('similar4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='similar4_of', to='api.Xonca')),
            ],
        ),
        migrations.CreateModel(
            name='Vitrin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=5.9, max_digits=6, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('ingredient', models.CharField(blank=True, max_length=511, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('publish', models.BooleanField(default=True)),
                ('homepage', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, default=7, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.VitrinCategory')),
                ('similar1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='similar1_of', to='api.Vitrin')),
                ('similar2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='similar2_of', to='api.Vitrin')),
                ('similar3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='similar3_of', to='api.Vitrin')),
                ('similar4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='similar4_of', to='api.Vitrin')),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Marsipan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=12.0, max_digits=6, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('ingredient', models.CharField(blank=True, max_length=511, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('publish', models.BooleanField(default=True)),
                ('homepage', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, default=4, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.MarsipanCategory')),
                ('similar1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='similar1_of', to='api.Marsipan')),
                ('similar2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='similar2_of', to='api.Marsipan')),
                ('similar3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='similar3_of', to='api.Marsipan')),
                ('similar4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='similar4_of', to='api.Marsipan')),
            ],
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=63)),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=12.0, max_digits=6, null=True)),
                ('discount', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('ingredient', models.CharField(blank=True, max_length=511, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('publish', models.BooleanField(default=True)),
                ('homepage', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, default=4, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.FlowerCategory')),
                ('similar1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='similar1_of', to='api.Flower')),
                ('similar2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='similar2_of', to='api.Flower')),
                ('similar3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='similar3_of', to='api.Flower')),
                ('similar4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='similar4_of', to='api.Flower')),
            ],
        ),
    ]