from django import template

register = template.Library()

@register.filter
def mul(value, arg):
    return value * arg

@register.filter
def sum_total(items):
    total = sum(item.cantidad * item.producto.precio for item in items)
    return total