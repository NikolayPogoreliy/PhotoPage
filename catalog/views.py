from django.shortcuts import render_to_response, render
from catalog.models import Category, Services, Materials
from django.conf import settings
from django.contrib.auth import get_user, context_processors as acp
from django.template import RequestContext, context_processors as tcp

# Create your views here.
def cust_user_proc(request):
    return {'user':get_user(request)}

def category_main(request):
    all_parrent_cat= Category.objects.filter(parent_id__isnull= True).order_by('ordering')
    return render(request, 'hompage.html',  {'cats':all_parrent_cat,},
                              context_instance=RequestContext(request, processors=[cust_user_proc,
                                                                                   tcp.request,
                                                                                   acp.auth,
                                                                                   ]),)


def services(request):
    return render_to_response('services.html', {'category': Category.objects.filter(parent_id__isnull= True).order_by('ordering')})

def category(request, slug):
    args={}

    category = Category.objects.get(slug=slug)

    args['short_description'] = category.shot_description
    args['description'] = category.description
    args['title'] = category.name
    args['user'] = get_user(request)
    args['meta_title'] = category.title
    args['meta_key'] = category.meta_key
    args['meta-desc'] = category.meta_desc

    categorys = Category.objects.filter(parent_id=category.id).order_by('ordering')
    args['category'] = categorys
    services = Services.objects.filter(category = category.id).order_by('material','ordering')
    args['services'] = services
    sizes = []
    for service in services:
        if not sizes.count(service.size):
            sizes.append(service.size)
    args['sizes'] = sizes
    return render_to_response('services.html', args)


