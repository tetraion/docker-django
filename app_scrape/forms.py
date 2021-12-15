from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets


widgets_textinput = forms.TextInput(
    attrs={
        "class": "form-control",
    }
)

class TextForm(forms.Form):
    
    search = forms.CharField(label="品名", widget=widgets_textinput)

class FavForm(forms.Form):
    name = forms.CharField(label="商品名", widget=widgets_textinput)
    price = forms.CharField(label="価格", widget=forms.Textarea(attrs={'cols': '80', 'rows': '10'}))
    url = forms.CharField(label="URL")


    
