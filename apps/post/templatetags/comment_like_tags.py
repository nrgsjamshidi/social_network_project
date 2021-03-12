from django import template

register = template.Library()


@register.simple_tag(name='numq')
def numq(obs, word):
    if len(obs) > 1 or len(obs) == 0:
        word = word + 's'
        return ' '.join([str(len(obs)), word])