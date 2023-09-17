from django import forms
from events.models import Comment, FotoUsers


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["content"]

        widgets = {

            "content": forms.TextInput(attrs={"class": "form-control"}),
        }


class FileForm(forms.ModelForm):

    class Meta:
        model = FotoUsers
        fields = ["foto"]
