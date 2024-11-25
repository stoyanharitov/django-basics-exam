from django.urls import path, include

from posts_app.views import PostCreateView, PostDetailView, PostEditView, PostDeleteView

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='create-post'),
    path('<int:post_id>/', include([
        path('details/', PostDetailView.as_view(), name='post-details'),
        path('edit/', PostEditView.as_view(), name='post-edit'),
        path('delete/', PostDeleteView.as_view(), name='post-delete')
    ]))
]