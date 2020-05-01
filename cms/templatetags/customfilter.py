from django import template


register = template.Library() # Djangoのテンプレートタグライブラリ

# カスタムフィルタとして登録する
@register.filter
def lineRep(value):
    value.replace(';', '\n')
    return value.replace('\n\n', '\n')

@register.filter
def lineSpace(value):
    return value.replace(';', ' ')