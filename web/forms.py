from django import forms

class PostForm(forms.Form):
    post_field = forms.CharField(widget=forms.Textarea)
