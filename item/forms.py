from django import forms

from .models import Items

# for avoide representation we make a class for disegning.
# FORM_INPUT_CLASS = 'w-1/2 px-3 py-2 rounded-xl border'
FORM_INPUT_CLASS = 'w-full text-left text-xl mt-2 px-3 py-2 rounded-xl !outline-none'

class NewItemForm(forms.ModelForm):
    class Meta:
        model= Items
        fields = ('Name', 'category', 'description', 'image','price',)

        widgets ={
            'Name': forms.TextInput(attrs={'class':FORM_INPUT_CLASS}),
            'category': forms.Select(attrs={'class':FORM_INPUT_CLASS}),
            'description': forms.Textarea(attrs={'class':FORM_INPUT_CLASS}),
            'image': forms.FileInput(attrs={'class':FORM_INPUT_CLASS}),
            'price': forms.TextInput(attrs={'class':FORM_INPUT_CLASS}),
        }


class EditItemForm(forms.ModelForm):
    class Meta:
        model= Items
        fields = ('Name', 'description', 'image','price','is_sold')

        widgets ={
            'Name': forms.TextInput(attrs={'class':FORM_INPUT_CLASS}),
            'description': forms.Textarea(attrs={'class':FORM_INPUT_CLASS}),
            'image': forms.FileInput(attrs={'class':FORM_INPUT_CLASS}),
            'price': forms.TextInput(attrs={'class':FORM_INPUT_CLASS}),
            # 'is_sold': forms.BooleanInput(attrs={'class':FORM_INPUT_CLASS}),
        }