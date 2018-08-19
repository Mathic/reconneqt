from django import template

register = template.Library()

@register.filter(name='get_occurence')
def get_occurence(value, total):
    percentage = (value / total) * 100
    # print(percentage)
    if percentage <= 25:
        return "sm"
    elif percentage > 65:
        return "lg"
    else:
        return "md"
