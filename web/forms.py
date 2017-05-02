from django import forms

from taggit.forms import *
class PostForm(forms.Form):
    post_title = forms.CharField()
    post_field = forms.CharField(widget=forms.Textarea(attrs={'class':'materialize-textarea'}))
    post_image = forms.ImageField()
    post_tags = TagField(widget=TagWidget())
