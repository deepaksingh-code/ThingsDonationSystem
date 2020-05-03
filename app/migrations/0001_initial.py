# Generated by Django 3.0.4 on 2020-03-13 05:54

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
                ('streetno', models.CharField(max_length=1024)),
            ],
        ),
        migrations.CreateModel(
            name='Donator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('dob', models.DateField()),
                ('mobileno', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Orphanage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Pincode',
            fields=[
                ('city', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('pincode', models.IntegerField(primary_key=True, serialize=False)),
                ('state', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=1024)),
                ('quantity', models.CharField(max_length=200)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Address')),
                ('donator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Donator')),
                ('orphanage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Orphanage')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='pin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Pincode'),
        ),
    ]
