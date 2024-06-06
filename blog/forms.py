from django import forms # type: ignore
from blog.models import  Comment
from blog.models import Customer
from django.db import models # type: ignore



class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email','phone',]   







class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['full_name', 'email', 'message']