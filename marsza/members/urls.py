from django.urls import path
from .views import UserRegister, UserEdit, PasswordChange, ShowProfilePage, EditProfilePage, CreateProfilePage
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path('register/', UserRegister.as_view(), name = 'register'),
   path('edit/', UserEdit.as_view(), name = 'edit_profile'),
   #path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
   path('password/', PasswordChange.as_view(template_name='registration/change_password.html')),
   path('password_success/', views.password_success, name='password_success'),
   path('<int:pk>/profile', ShowProfilePage.as_view(), name='user_profile'),
   path('<int:pk>/edit/profile_page/', EditProfilePage.as_view(), name='edit_profile_page'),
   path('create/profile_page/', CreateProfilePage.as_view(), name='create_profile_page'),
]