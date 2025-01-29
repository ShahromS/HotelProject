# orders/forms.py
from django import forms
from .models import Restaurant, RestaurantImage
from .widgets import MultipleFileInput



class RestaurantImageForm(forms.ModelForm):
    class Meta:
        model = RestaurantImage
        fields = ['image']
        widgets = {
            'image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'layout_image']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter restaurant name'
            }),
            'layout_image': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }

    def clean_layout_image(self):
        image = self.cleaned_data.get('layout_image')
        if not image:
            raise forms.ValidationError("Please select an image file")
        return image
class UploadLayoutForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'layout_image']


class MultiImageUploadForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['name', 'layout_image']  # Field for the main layout image

    additional_images = forms.FileField(widget=MultipleFileInput, required=False) # Field for additional images

    def save(self, commit=True):
        instance = super().save(commit=commit) # Save the Restaurant instance first
        for image in self.files.getlist('additional_images'): # Save additional images
            RestaurantImage.objects.create(restaurant=instance, image=image)
        return instance