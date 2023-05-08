from django import forms
from .models import Comments


class CommentsFrom(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('name', 'email', 'text_coments')
