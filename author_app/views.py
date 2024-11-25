from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from author_app.forms import AuthorCreateForm, AuthorEditForm
from author_app.models import Author
from reg_exam_main.utils import get_active_user


# VIEWS
class AuthorCreateView(CreateView):
    model = Author
    template_name = 'app_author/create-author.html'
    form_class = AuthorCreateForm
    success_url = reverse_lazy('post-dashboard')

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'app_author/details-author.html'
    context_object_name = 'author'

    def get_object(self, queryset=None):
        return get_active_user()


class AuthorEditView(UpdateView):
    model = Author
    form_class = AuthorEditForm
    template_name = 'app_author/edit-author.html'
    context_object_name = 'author'
    success_url = reverse_lazy('author-details')

    def get_object(self, queryset=None):
        return get_active_user()

class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'app_author/delete-author.html'
    success_url = reverse_lazy('index-page')

    def get_object(self, queryset=None):
        return get_active_user()
