from django.urls import path, include

from accounts import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.Registration.as_view(), name='registration'),
]