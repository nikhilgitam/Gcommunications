import ast
import datetime

from django import template
from django.contrib.auth.models import Group

register = template.Library()
from django.utils.safestring import mark_safe

@register.filter(name='has_group')
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()


@register.filter
def get_scholar_status(status):
    s = {'1': 'Active', '2': 'Inactive', '3': 'Awarded', '4': 'Discontinued', '5': 'Terminated', '6': 'Terminated'}
    return s[str(status)]


@register.filter(name='encrypting')
def encrypting(id):
    encrypt_id = encrypt(id)
    return encrypt_id

@register.simple_tag
def datetime_local_with_min():


    dt_now = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M')

    return dt_now


@register.filter(name='to_int')
def to_int(value):
    try:
        return int(float(value))
    except:
        return value

@register.filter(name='from_current_data')
def from_current_data(value):
    try:
        today = datetime.date.today()
        s = str(today)
        return s
    except:
        return 0


@register.filter(name='my_wordcount')
def my_wordcount(value):
    """Return the number of words."""
    data = value.split(" ")

