from django import template

register = template.Library()

@register.filter
def age_pluralize(age):
    age = str(age)
    if   age[-1] in '1':
            return('год')
    elif age[-1] in '234':
        return('года')
    else:
            return('лет')