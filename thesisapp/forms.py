from django.forms import ModelForm
from .models import Comment, Thesis

class CommentForm(ModelForm):
    class Meta:
        model = Comment 
        fields = ['name', 'email', 'body']
