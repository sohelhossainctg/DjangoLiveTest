from django.shortcuts import render
from django.http import HttpResponse
from contact_info.models import Contact
# from . import forms

def home(request):
  data = Contact.objects.all()
  total_contacts = data.count()
  context = {
    "data" : data,
     "total_contacts" : total_contacts,
  }
  return render(request, 'home.html', context=context)
