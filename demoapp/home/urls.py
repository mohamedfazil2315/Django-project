from django.urls import path
from .views import index, login_view, signup_view

urlpatterns = [
    path('', index),
    path('login/', login_view),
    path('signup/', signup_view),
]
