import re

from django.core.exceptions import ValidationError


def validate_username(value):
    if not bool(re.match(r'^[\w.@+-]+$', value)):
        raise ValidationError(
            'В имени пользователя недопустимые символы'
        )
    return value