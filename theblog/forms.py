from django import forms
# from django.forms import fields, widgets
from .models import Post, Category

choices = Category.objects.all().values_list('name','name')
print(choices)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'body','snippet', 'category', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'id':'author', 'type':'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control', "id":"author", '':''}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices,attrs={'class': 'form-control'}),
            'header_image': forms.FileInput(attrs={'class': 'form-control'})

        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'snippet', 'category', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choices, attrs={'class': 'form-control'}),
            'header_image': forms.FileInput(attrs={'class': 'form-control'}),

        }