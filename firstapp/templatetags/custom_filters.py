from django import template

register = template.Library()

@register.filter
# replace _ with ' ', allowing filenames and underscores in URL paths but not displayed
# this is used in base.html and painting_list.html, where the category name is displayed
def replace_chars(value):
    return value.replace('_', ' ')
