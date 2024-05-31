from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label="Name")
    email = forms.EmailField(max_length=254, required=True)
    subject = forms.CharField(max_length=100, required=True)
    message = forms.CharField(
        widget=forms.Textarea, min_length=5, max_length=1000, required=True
    )
    captcha = forms.CharField(max_length=5, required=True, label="2 + 3 = ?")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        return email

    def clean_captcha(self):
        captcha = self.cleaned_data.get("captcha")
        if captcha != "5":
            raise forms.ValidationError("Incorrect answer for CAPTCHA.")
        return captcha
