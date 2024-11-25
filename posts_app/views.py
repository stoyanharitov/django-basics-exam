from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from author_app.models import Author
from posts_app.forms import PostCreateForm, PostEditForm, PostDeleteForm
from posts_app.models import Post


# VIEWS
class PostDashboardView(ListView):
    model = Post
    template_name = 'app_posts/dashboard.html'
    context_object_name = 'posts'
    ordering = ['-updated_at']

class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    success_url = reverse_lazy('post-dashboard')
    template_name = 'app_posts/create-post.html'

    def form_valid(self, form):
        form.instance.author = Author.objects.first()
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Post
    pk_url_kwarg = 'post_id'
    template_name = 'app_posts/details-post.html'
    context_object_name = 'post'

class PostEditView(UpdateView):
    model = Post
    form_class = PostEditForm
    success_url = reverse_lazy('post-dashboard')
    pk_url_kwarg = 'post_id'
    template_name = 'app_posts/edit-post.html'


class PostDeleteView(DeleteView):
    model = Post
    form_class = PostDeleteForm
    pk_url_kwarg = 'post_id'
    success_url = reverse_lazy('post-dashboard')
    template_name = 'app_posts/delete-post.html'

    def get_initial(self):
        return self.object.__dict__

    def form_invalid(self, form):
        return self.form_valid(form)