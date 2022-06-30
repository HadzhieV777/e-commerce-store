from django import forms
from core_helpers.form_mixins import FormFieldsController
from .models import Comment

class CommentForm(forms.ModelForm, FormFieldsController):
    class_name = "form-control"
    placeholders = {
        "user_name": "Name",
        "user_email": "Email Address",
        "text": "Review"
    }
    
    class Meta:
        model = Comment
        labels = {'user_name': 'Name', 'user_email': 'Email', 'text': 'Review'}
        fields = ('user_name', 'user_email', 'text')
    
    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        super(CommentForm, self).set_up_fields()