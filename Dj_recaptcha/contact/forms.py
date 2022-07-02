
from django import forms
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
  
  
class ContactForm(forms.Form):
    firstName = forms.CharField()
    LastName = forms.CharField()
    email = forms.EmailField()
    PhoneNumber = forms.IntegerField()
    Complaint = forms.CharField(widget=forms.Textarea)
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)