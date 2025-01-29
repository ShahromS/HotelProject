# Generated by Django 5.1.3 on 2025-01-20 12:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_type', models.CharField(max_length=50)),
                ('x_position', models.FloatField()),
                ('y_position', models.FloatField()),
                ('width', models.FloatField()),
                ('height', models.FloatField()),
                ('confidence', models.FloatField(default=0.0)),
                ('is_occupied', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('layout_image', models.ImageField(blank=True, null=True, upload_to='restaurant_layouts/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('furniture', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='orders.furniture')),
            ],
        ),
        migrations.AddField(
            model_name='furniture',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='furniture', to='orders.restaurant'),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('capacity', models.IntegerField()),
                ('is_available', models.BooleanField(default=True)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='orders.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('x_position', models.FloatField(default=0)),
                ('y_position', models.FloatField(default=0)),
                ('width', models.FloatField(default=100)),
                ('height', models.FloatField(default=100)),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tables', to='orders.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Chair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x_offset', models.FloatField(default=0)),
                ('y_offset', models.FloatField(default=0)),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chairs', to='orders.table')),
            ],
        ),
    ]
