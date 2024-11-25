from author_app.models import Author

def get_active_user():
    return Author.objects.first()