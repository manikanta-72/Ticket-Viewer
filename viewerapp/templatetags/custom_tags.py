from django import template

register = template.Library()

def date_time(value):
    value = value[:-1]
    return value.split("T")[0] + ' ' + value.split("T")[1]

register.filter('date_time', date_time)