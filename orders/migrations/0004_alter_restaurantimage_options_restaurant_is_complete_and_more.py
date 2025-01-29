# Generated by Django 5.1.3 on 2025-01-22 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_restaurantimage_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='restaurantimage',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='restaurant',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='photo_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='total_width',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='restaurantimage',
            name='offset_x',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='restaurantimage',
            name='offset_y',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='restaurantimage',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='restaurantimage',
            name='overlap_width',
            field=models.FloatField(default=0),
        ),
    ]
