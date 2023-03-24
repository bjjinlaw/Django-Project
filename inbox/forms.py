from django import forms
from inbox.models import Message

class InboxForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ("description", )