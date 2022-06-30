from django.core.exceptions import ValidationError


def validate_password_contains_uppercase_letter(value: str):
    if not any([char.isupper() for char in value]):
        raise ValidationError("Password must contain at least one uppercase letter.")


def validate_password_contains_lowercase_letter(value: str):
    if not any([char.islower() for char in value]):
        raise ValidationError("Password must contain at least one lowercase letter.")

def validate_password_contains_digit(value: str):
    if not any([char.isdigit() for char in value]):
        raise ValidationError("Password must contain at least one digit.")

def validate_password_contains_special_symbol(value: str):
     special_sym =['$', '@', '#', '%', '*']
     if not any([char in special_sym for char in value]):
         raise ValidationError("Password must contain at least one special symbol($, @, #, %, *).")
        