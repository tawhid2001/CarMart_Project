from django.urls import path
from  . import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.UserLoginView.as_view(),name='login'),
    path('logout/',views.UserLogout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile/edit/',views.editProfile,name='edit_profile'),
]