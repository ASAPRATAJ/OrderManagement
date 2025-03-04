"""
Custom validators for the 'users' app.
Defines password validation rules for the CustomUser model.
"""

import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class CustomPasswordValidator:
    """
    Custom password validator requiring:
    - At least one lowercase letter
    - At least one uppercase letter
    - At least one digit
    - At least one special character from: !@#$%^&*(),.?":{}|<>
    - Minimum length of 8 characters
    """

    SPECIAL_CHARS = r'[!@#$%^&*(),.?":{}|<>]'
    MIN_LENGTH = 8

    def validate(self, password, user=None):
        """Validate the password against custom rules."""
        if len(password) < self.MIN_LENGTH:
            raise ValidationError(
                _("Password must be at least %(min_length)d characters long."),
                params={"min_length": self.MIN_LENGTH},
            )
        if not any(char.islower() for char in password):
            raise ValidationError(_("Password must contain at least one lowercase letter."))
        if not any(char.isupper() for char in password):
            raise ValidationError(_("Password must contain at least one uppercase letter."))
        if not any(char.isdigit() for char in password):
            raise ValidationError(_("Password must contain at least one digit."))
        if not re.search(self.SPECIAL_CHARS, password):
            raise ValidationError(_("Password must contain at least one special character."))

    def get_help_text(self):
        """Return a help text describing the password requirements."""
        return _(
            "Your password must contain at least %(min_length)d characters, "
            "including one lowercase letter, one uppercase letter, one digit, "
            "and one special character (e.g., !@#$%^&*(),.?\":{}|<>)."
        ) % {"min_length": self.MIN_LENGTH}
