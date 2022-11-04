from accounts import views

from django.urls import include, path


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.Registration.as_view(), name='registration'),
]
