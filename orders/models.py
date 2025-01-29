# orders/models.py
from django.db import models
from django import forms

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    layout_image = models.ImageField(
        upload_to='restaurant_layouts/',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Проверяем, есть ли старое изображение
        if self.pk:
            try:
                old_instance = Restaurant.objects.get(pk=self.pk)
                if old_instance.layout_image and self.layout_image != old_instance.layout_image:
                    # Удаляем старое изображение
                    old_instance.layout_image.delete(False)
            except Restaurant.DoesNotExist:
                pass
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Удаляем файл изображения при удалении объекта
        if self.layout_image:
            self.layout_image.delete(False)
        super().delete(*args, **kwargs)

class RestaurantImage(models.Model):
    restaurant = models.ForeignKey(Restaurant, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='restaurant_layouts/')
    order = models.IntegerField(default=0)
    offset_x = models.FloatField(default=0)  # Смещение по X относительно начала
    offset_y = models.FloatField(default=0)  # Смещение по Y для выравнивания
    overlap_width = models.FloatField(default=0)  # Ширина перекрытия с предыдущим изображением

    class Meta:
        ordering = ['order']


class Table(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='tables')
    number = models.IntegerField()
    x_position = models.FloatField(default=0)
    y_position = models.FloatField(default=0)
    width = models.FloatField(default=100)
    height = models.FloatField(default=100)

    def __str__(self):
        return f"Table {self.number}"

class Chair(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='chairs')
    x_offset = models.FloatField(default=0)
    y_offset = models.FloatField(default=0)

    def __str__(self):
        return f"Chair for Table {self.table.number}"

class Furniture(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='furniture')
    object_type = models.CharField(max_length=50)
    x_position = models.FloatField()
    y_position = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    confidence = models.FloatField(default=0.0)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.object_type} at ({self.x_position}, {self.y_position})"

class Room(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='rooms')
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='orders')
    detail = models.TextField()
    status = models.CharField(max_length=10, choices=[('pending', 'Pending'), ('served', 'Served')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order for {self.table}"

class UploadLayoutForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'layout_image']