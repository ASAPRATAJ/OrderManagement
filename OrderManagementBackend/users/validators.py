import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class CustomPasswordValidator:
    """
    Własny walidator haseł, który wymaga:
    - co najmniej jednej małej litery,
    - co najmniej jednej dużej litery,
    - co najmniej jednej cyfry,
    - co najmniej jednego znaku specjalnego.
    """
    def validate(self, password, user=None):
        if not any(char.islower() for char in password):
            raise ValidationError(_("Hasło musi zawierać co najmniej jedną małą literę."))
        if not any(char.isupper() for char in password):
            raise ValidationError(_("Hasło musi zawierać co najmniej jedną dużą literę."))
        if not any(char.isdigit() for char in password):
            raise ValidationError(_("Hasło musi zawierać co najmniej jedną cyfrę."))
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError(_("Hasło musi zawierać co najmniej jeden znak specjalny."))

    def get_help_text(self):
        return _(
            "Hasło musi zawierać co najmniej jedną małą literę, "
            "jedną dużą literę, jedną cyfrę oraz jeden znak specjalny."
        )
