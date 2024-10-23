from django import template

register = template.Library()

CENSOR_WORDS = ['блатняк', 'шансон',]

@register.filter()
def censor(value):
    """
    value: text_news
    """
    words = value.split()
    for i in range(len(words)):
        if words[i].lower() in CENSOR_WORDS:
            words[i] = words[i][0] + '*' * (len(words[i]) - 1)

    return ' '.join(words)
