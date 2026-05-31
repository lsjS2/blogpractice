from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path("", views.BlogList.as_view(), name="blog_list"),
    path("<int:pk>/", views.BlogDetail.as_view(), name="blog_detail"),
    path("<int:pk>/comments/", views.CommentList.as_view(), name="comment_list"),
]