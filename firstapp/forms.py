from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField(max_length=254, required=True)
    message = forms.CharField(widget=forms.Textarea, min_length=5, max_length=1000, required=True)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        return email

