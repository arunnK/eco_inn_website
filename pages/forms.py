from django import forms
from captcha.fields import ReCaptchaField
	
class ContactForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'value': 'Name'}))
	subject = forms.CharField(widget=forms.TextInput(attrs={'value': 'Subject', 'size' : '100'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'default': 'No msg'}))
	sender = forms.EmailField(widget=forms.TextInput(attrs={'value': 'Email'}))
	captcha = ReCaptchaField(attrs={'theme' : 'clean'})

class JoinForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'value': 'Name'}))
	rollno = forms.CharField(widget=forms.TextInput(attrs={'value': 'Roll no.'}))
	mobno = forms.CharField(widget=forms.TextInput(attrs={'value': 'Mobile'}))
	branch = forms.CharField(widget=forms.TextInput(attrs={'value': 'Branch', 'size' : '100'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'default': 'NIL'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'value': 'Email'}))
	captcha = ReCaptchaField(attrs={'theme' : 'clean'})

class SignUpForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'value': 'Name'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'value': 'Email'}))
	captcha = ReCaptchaField(attrs={'theme' : 'clean'})