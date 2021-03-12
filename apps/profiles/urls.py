from django.urls import path
from . import views
from apps.profiles.views import edit_my_profile_view

app_name = 'profiles'

urlpatterns = [
    path('edit_myprofile/', edit_my_profile_view, name='my_profile_view'),
    # path('my-profile/', views.my_profile, name='my_profile'),
    path('profile/<first_name>/', views.profile_view, name='profile_view'),
    ]
