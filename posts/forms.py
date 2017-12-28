from .models import Post
from django import forms

class postForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=[
            "title",
            "content"
        ]
