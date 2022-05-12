from django.forms import ModelForm, TextInput, EmailInput, Textarea
from .models import Message

# Create the form class.
class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control rounded-0',
                'placeholder': 'Name'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control rounded-0',
                'placeholder': 'Email'
            }),
            'subject': TextInput(attrs={
                'class': 'form-control rounded-0',
                'placeholder': 'Subject'
            }),
            'message': Textarea(attrs={
                'class': 'form-control rounded-0',
                'placeholder': 'Message',
                'rows': '8'
            })
        }