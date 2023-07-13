from django import forms
from .models import Comment, Post


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ("comment",)
        
class AddPostForm(forms.ModelForm): 
    class Meta:
        model = Post
        fields = ("title","status", "body",)
        