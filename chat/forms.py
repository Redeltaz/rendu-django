from dataclasses import field
from django import forms
from .models import Message 

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message

        fields = "__all__"

        widgets = {
            'content': forms.TextInput(attrs={'class': 'chat-input', 'placeholder': 'content'})
        }