from django import template

register = template.Library()


@register.filter(name="dots")
def dots(value, maximum=5):
    if value > maximum:
        maximum = 10
    return "●" * value + "○" * (maximum - value)
