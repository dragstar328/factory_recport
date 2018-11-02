from django import forms
from django.forms import TextInput, Textarea, ClearableFileInput
from .models import Post, Comment

class PostForm(forms.ModelForm):

  class Meta:
    model = Post
    fields = ('title', 'text', 'image',)


class CommentForm(forms.ModelForm):

  class Meta:
    model = Comment
    fields = ('author', 'text',)
