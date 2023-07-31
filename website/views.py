from django.shortcuts import render
#from django.http import HttpResponse
#from website.models import Contact
from website.forms import  ContactForm,NewsLetterForm
from django.contrib import messages

def index_view(request):
    return render(request,'website/index.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Thanks . Your message has been received.')
    form = ContactForm()
    return render(request,'website/contact.html',{'form':form})


def about_view(request):
    return render(request,'website/about.html')

def letter_view(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'website/index.html')
    else:
        return render(request,'website/index.html')
    form = NewsLetterForm()
