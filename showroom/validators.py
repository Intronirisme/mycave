from django.core.exceptions import ValidationError
import datetime

#my custom validation functions

def noFuture(value):
    if value > datetime.date.today().year:
        raise ValidationError("Go away Dr. Brown !")
    return value