from django import template

register = template.Library()


@register.filter(name='teste')
def teste(id):
    return f"seu valor {id}"
