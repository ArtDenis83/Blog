from django import forms
from .models import BlogPost

class BlogForm(forms.ModelForm):
    class Meta():
        model = BlogPost
        fields = ["text"]
        labels = {"text": ""}
        widgets = {"text": forms.Textarea(attrs={'cols': 100})}
