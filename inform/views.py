from django.shortcuts import render_to_response
from inform.models import AboutUs, Contacts, ContactType
from django.contrib.auth import get_user
from django.core.context_processors import csrf
# Create your views here.

def about(request):
    about_us = AboutUs.objects.all().latest('pub_date')
    meta_title = about_us.title
    return render_to_response('about_us.html', {'cont': about_us, 'meta_title': meta_title, 'user': get_user(request)})

def contacts(request):
    soc_id = ContactType.objects.get(name='social').id
    args={}
    args['cnts'] = Contacts.objects.exclude(name=soc_id).order_by('name_id', 'contact')
    args['social'] = Contacts.objects.filter(name=soc_id)
#    return render_to_response('contacts.html', {'cnts':Contacts.objects.all().order_by('type_id', 'contact'), 'user': get_user(request)})
    return  render_to_response('contacts.html', args)