from django import template
register = template.Library()

from inform.models import Contacts


@register.inclusion_tag('header_contacts.html')
def show_header_contacts(cont_id=1):
    conts = Contacts.objects.filter(name_id = cont_id)
    name = conts[0].name
    return {'head_conts':conts, 'name':name}