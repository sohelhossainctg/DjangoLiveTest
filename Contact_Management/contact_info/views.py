from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
from . import forms

def add_contact(request):
    if request.method == 'POST':
        contact_form = forms.ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('homepage')
        else:
            return render(request, 'add_contact.html', {'form': contact_form})
    else:
        contact_form = forms.ContactForm()    
        return render(request, 'add_contact.html', {'form': contact_form})
    
def update_contact(request, id):
    try:
        contact = Contact.objects.get(id=id)
    except Contact.DoesNotExist:
        return HttpResponse("Contact not found")

    if request.method == 'POST':
        contact_form = forms.ContactForm(request.POST, instance=contact)
        if contact_form.is_valid():
            contact_form.save()
            return redirect('add_contact')
    else:
        contact_form = forms.ContactForm(instance=contact)
    
    return render(request, 'update_contact.html', {'form': contact_form})

def delete_contact(request, id):
    try:
        contact = Contact.objects.get(id=id)
        contact.delete()
        return redirect('edit_contact')
    except Contact.DoesNotExist:
        return HttpResponse("Contact not found")


def home(request):
  data = Contact.objects.all()
  return render(request, 'edit_contacts.html', {'data': data})

def view_profile(request, id):
    try:
        data = Contact.objects.get(id=id)
        return render(request, 'view_profile.html', {'data': data})
    except Contact.DoesNotExist:
        return HttpResponse("<h1>Contact not found</h1>")
    
    
    