from django import forms
from website.models import Contact,NewsLetter
from captcha.fields import CaptchaField



class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = '__all__'
        
class ContactForm(forms.ModelForm):
    captcha = CaptchaField() 
    def clean_subject(self):
        return ''
    
    class Meta:
        model = Contact
        fields = ['subject']