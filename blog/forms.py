from django import forms
from django.forms import TextInput, Textarea, ClearableFileInput
from .models import Post

class PostForm(forms.ModelForm):

  class Meta:
    model = Post
    fields = ('title', 'text', 'image',)

    '''
    widgets = {
      'title': TextInput(attrs={'class': 'form-control'}),
      'text': Textarea(attrs={'class': 'form-control'}),
      'image': ClearableFileInput(attrs={'class': 'form-control-file'}),
    }
    '''
    
