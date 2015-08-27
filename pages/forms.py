from django import forms
from captcha.fields import ReCaptchaField

class ContactForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'value': 'Name'}))
	subject = forms.CharField(widget=forms.TextInput(attrs={'value': 'Subject', 'size' : '100'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'default': 'No msg'}))
	sender = forms.EmailField(widget=forms.TextInput(attrs={'value': 'Email'}))
	captcha = ReCaptchaField(attrs={'theme' : 'clean'})

class JoinForm(forms.Form):
	first_name = forms.CharField(widget=forms.TextInput(attrs={'size' : '30'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'size' : '30'}))
	rollno = forms.CharField(widget=forms.TextInput(attrs={'size' : '10'}))
	mobno = forms.CharField(widget=forms.TextInput(attrs={'size' : '13'}))
	branch = forms.CharField(widget=forms.TextInput(attrs={'size' : '30'}))
	message = forms.CharField(widget=forms.Textarea(attrs={'size' : '500'}))
	email = forms.EmailField(widget=forms.TextInput())
	captcha = ReCaptchaField(attrs={'theme' : 'clean'})

class SignUpForm(forms.Form):
	name = forms.CharField(widget=forms.TextInput(attrs={'value': 'Name'}))
	email = forms.EmailField(widget=forms.TextInput(attrs={'value': 'Email'}))
	captcha = ReCaptchaField(attrs={'theme' : 'clean'})
