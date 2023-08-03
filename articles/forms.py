from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "email"}),
    )
    name = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "name"}),
    )
    is_author = forms.BooleanField(required=False)
    is_publisher = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = (
            "username",
            "name",
            "email",
            "password1",
            "password2",
            "is_author",
            "is_publisher",
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "User Name"
        self.fields["username"].label = ""
        self.fields[
            "username"
        ].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password1"].label = ""
        self.fields[
            "password1"
        ].help_text = "<ul class=\"form-text text-muted small\"><li>Your password can't be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can't be a commonly used password.</li><li>Your password can't be entirely numeric.</li></ul>"
        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs["placeholder"] = "Confirm Password"
        self.fields["password2"].label = ""
        self.fields[
            "password2"
        ].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
        self.fields["is_author"].label = "is_author"
        self.fields["is_publisher"].label = "is_publisher"


class AddArticles(forms.ModelForm):
    title = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": " title", "class": "form-control"}
        ),
        label="",
    )
    subtitle = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "subtitle", "class": "form-control"}
        ),
        label="",
    )
    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 20, 'cols': 170,"placeholder": "content"}),label="") 
    thumbnail = forms.ImageField(
        widget=forms.widgets.FileInput(
            attrs={"placeholder": "Image", "class": "form-control", "required": False}
        ),
        label="",  
    )
    
    class Meta:
        model = Articles
        fields = ['title', 'subtitle', 'content', 'thumbnail']
        exclude = ('author','publisher','status')
