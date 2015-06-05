from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from .forms import ContactForm,JoinForm
from django.core.mail import send_mail
# Create your views here.

def home(request):
	return render_to_response("pages/home.html")


#def contact(request):
	#return render_to_response("pages/contact.html")

def about(request):
	return render_to_response("pages/about.html")

def activities(request):
	return render_to_response("pages/activities.html")

def ps(request):
	return render_to_response("pages/problemstatements.html")

def contact(request):
	if request.method == 'POST': # If the form has been submitted...
	# ContactForm was defined in the previous section
		form = ContactForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			name =  form.cleaned_data['name']
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']
			recipients = ['innovationecosystem.nith@gmail.com']
			send_mail(subject, message+'\n'+name, sender, recipients)
			return render(request, 'pages/home.html');
	else:
		form = ContactForm() # An unbound form
	return render(request, 'pages/contact.html', {
	'form': form,
	})

def join(request):
	if request.method == 'POST': # If the form has been submitted...
	# ContactForm was defined in the previous section
		form = JoinForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			name =  form.cleaned_data['name']
			rollno =  form.cleaned_data['rollno']
			mobno =  form.cleaned_data['mobno']
			branch = form.cleaned_data['branch']
			message = form.cleaned_data['message']
			email = form.cleaned_data['email']
			recipients = ['innovationecosystem.nith@gmail.com']
			send_mail('New Applicant '+name, 'Name -  '+name+'\n'+'Rollno -   '+rollno+'\n'+'Mobile -   '+mobno+'\n'+'Branch -   '+branch+'\n'+'Message -   '+message+'\n'+email,email, recipients)
			return render(request, 'pages/home.html');
	else:
		form = JoinForm() # An unbound form
	return render(request, 'pages/join.html', {
	'form': form,
	})