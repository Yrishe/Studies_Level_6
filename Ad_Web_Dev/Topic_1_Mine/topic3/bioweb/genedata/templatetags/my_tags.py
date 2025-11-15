import datetime 
from django import template
from ..models import Gene

register = template.Library()

@register.simple_tag
def todays_date():
    return datetime.datetime.now().strftime("%d %b, %Y")

@register.simple_tag
def author(name):
    return str(name)

@register.simple_tag
def get_total_genes():
    genes = Gene.objects.count()
    return genes