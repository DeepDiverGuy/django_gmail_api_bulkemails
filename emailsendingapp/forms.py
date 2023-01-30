from django import forms



class emails_form(forms.Form):
    
    emails = forms.CharField(widget=forms.Textarea(attrs={"rows":"20", "cols":"130"}))


