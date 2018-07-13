from django import forms
from  .models import Comment


class CommentFrom(forms.ModelForm):
    '''from表单提交'''
    class Meta:
        model = Comment
        fields = ['user_name', 'user_email', 'user_url', 'content']
