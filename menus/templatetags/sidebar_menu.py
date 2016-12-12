from django import template
register = template.Library()

from catalog.models import Category


@register.simple_tag
def show_sidebar_menu():
    return (Category.objects.filter(level=0).order_by('ordering'))#(Category.objects.all().order_by('tree_id','level','parent_id','ordering'))

@register.simple_tag
def show_sidebar_submenu(parent):
    return (Category.objects.filter(parent_id=parent).order_by('ordering'))#(Category.objects.all().order_by('tree_id','level','parent_id','ordering'))
