from django.core.validators import MinLengthValidator
from author_app.validators import NameValidator, PasscodeValidator
from django.db import models

from posts_app.models import Post


# Models
class Author(models.Model):
    first_name = models.CharField(max_length=40,
                                null=False,
                                blank=False,
                                validators=[MinLengthValidator(4),
                                            NameValidator()])

    last_name = models.CharField(max_length=50,
                                 null=False,
                                 blank=False,
                                 validators=[MinLengthValidator(2),
                                             NameValidator()])

    passcode = models.CharField(max_length=6,
                                null=False,
                                blank=False,
                                help_text="Your passcode must be a combination of 6 digits",
                                validators=[PasscodeValidator()])

    pets_number = models.PositiveSmallIntegerField(null=False,
                                blank=False)

    info = models.TextField(null=True,
                                blank=True)

    image_url = models.URLField(null=True,
                                blank=True)

    def get_last_post(self):
        return Post.objects.order_by('-updated_at').first()