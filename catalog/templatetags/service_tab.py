from django import template
register = template.Library()

from catalog.models import Materials

@register.inclusion_tag('material.html')
def show_material_desc(material_id):
    material= Materials.objects.get(id=material_id)
    return {'material': material}