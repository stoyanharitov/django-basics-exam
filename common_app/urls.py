from django.urls import path
from common_app.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index-page'),
]