from django.views.generic import TemplateView


# VIEWS
class  IndexView(TemplateView):
    template_name = 'index.html'