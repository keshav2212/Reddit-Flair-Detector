from flair import views
from django.urls import path

urlpatterns = [
    path('',views.home),
    path('automated_testing',views.testing),
]
