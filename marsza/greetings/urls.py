from django.urls import path
from .views import *

app_name="greetings"
urlpatterns = [
    path('', welcome, name="welcome"),
]