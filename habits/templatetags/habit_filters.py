from django import template
import datetime, humanfriendly

register = template.Library()

@register.filter(name='get_occurence')
def get_occurence(value, total):
    percentage = (value / total) * 100
    # print(percentage)
    if percentage <= 25:
        return "info"
    elif percentage > 65:
        return "warning"
    else:
        return "dark"

@register.filter(name='get_duration')
def get_duration(start, end):
    if end != None:
        total = end - start
        hours, remainder = divmod(total.total_seconds(), 3600)
        minutes, seconds = divmod(remainder, 60)
        duration = 'for '
        if int(hours) != 0:
            duration += str(int(hours)) + 'h '
        if int(minutes) != 0:
            duration += str(int(minutes)) + 'm '
        if int(seconds) != 0:
            duration += str(int(seconds)) + 's'

        return duration
    else:
        return ''
