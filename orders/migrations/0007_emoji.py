# Generated by Django 5.1.3 on 2025-01-28 21:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_order_furniture_order_status_order_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emoji',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emoji', models.CharField(max_length=10)),
                ('chair', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emojis', to='orders.chair')),
            ],
        ),
    ]
