from django.urls import path
from .views import *

app_name="blog"
urlpatterns = [
    path('', Homepage.as_view(), name="home"),
    path('add/', AddPost.as_view(), name="add_post"),
    path('add/category/', AddCategory.as_view(), name="add_category"),
    path('<int:pk>/', PostDetails.as_view(), name="post_details"),
    path('edit/<int:pk>/', EditPost.as_view(), name="edit_post"),
    path('delete/<int:pk>/', DeletePost.as_view(), name="delete_post"),
    path('category/<str:cat>/', CategoryPage, name="category"),
    path('like/<int:pk>/', Like, name="like_post"),
    path('post/<int:pk>/comment/', AddComment.as_view(), name="add_comment"),
    path('edit/comment/<int:pk>/', EditComment.as_view(), name="edit_comment"),
    path('delete/comment/<int:pk>/', DeleteComment.as_view(), name="delete_comment"),
]