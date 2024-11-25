from django.db import models
from django.core.validators import MinLengthValidator

# MODELS
class Post(models.Model):
    title = models.CharField(max_length=50,
                            null = False,
                            blank = False,
                            unique = True,
                            validators = [MinLengthValidator(5)],
                            error_messages = {'unique': "Oops! That title is already taken. How about something fresh and fun?"})

    image_url = models.URLField(null = False,
                                blank = False,
                                help_text="Share your funniest furry photo URL!")

    content = models.TextField(null = False, blank = False)

    updated_at = models.DateTimeField(auto_now=True,
                                      null=False,
                                      blank=False)

    author = models.ForeignKey(
        to='author_app.Author',
        on_delete=models.CASCADE,
        related_name="posts"
    )

    def first_three_words_content(self):
        words = self.content.split()

        if len(words) <= 3:
            return self.content.split()
        return ' '.join(words[:3])