from django.urls import path
from .views import AddCommentView

app_name = 'rating'

urlpatterns = (
    path('review/<slug:slug>', AddCommentView.as_view(), name='add review'),
)