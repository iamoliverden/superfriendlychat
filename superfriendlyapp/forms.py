from django.forms import ModelForm
from django import forms
from .models import *


class ChatMessageCreateForm(ModelForm):
    class Meta:
        model = Message
        fields = ['body']
        widgets = {
            'body': forms.TextInput(
                attrs={'placeholder': 'Type your message here...', 'class': 'p-4 text-black', 'maxlength': '500',
                       'autofocus': True}),
        }


class NewGroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['group_name']
        widgets = {
            'group_name': forms.TextInput(attrs={
                'placeholder': 'Type the name here...',
                'class': 'p-4 text-black',
                'maxlength': '200',
                'autofocus': True,
            }),
        }


class ChatRoomEditForm(ModelForm):
    class Meta:
        model = Group
        fields = ['group_name']
        widgets = {
            'group_name': forms.TextInput(attrs={
                'class': 'p-4 text-xl font-bold mb-4',
                'maxlength': '200',
            }),
        }


class NewGroupForm(ModelForm):
    class Meta:
        model = Group
        fields = ['groupchat_name']
        widgets = {
            'groupchat_name': forms.TextInput(attrs={
                'placeholder': "Add group chat name...",
                'class': 'p-4 text-black',
                'maxlength': '300',
                'autofocus': True,
            }),
        }


class ChatRoomEditForm(ModelForm):
    class Meta:
        model = Group
        fields = ['groupchat_name']
        widgets = {
            'groupchat_name': forms.TextInput(attrs={
                'class': 'p-4 text-black',
                'maxlength': '300',
        }),
        }