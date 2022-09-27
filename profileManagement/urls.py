from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile_generic_view.as_view()),
]