from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ('name', 'email', 'body')
    widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите ваше имя'}),
            'email': forms.TextInput(attrs={'placeholder': 'Введите Ваш e-mail'}),
            'body': forms.Textarea(attrs={'placeholder': 'Введите текст комментария'}),
        }



class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)