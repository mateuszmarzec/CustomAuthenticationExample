from django.urls import path
from django.contrib.auth import views

from App.views import SignUpView, IndexView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup-view'),
    path('signin/', views.LoginView.as_view(template_name='registration/signin.html'), name='signin-view'),
    path('signout/', views.LogoutView.as_view(), name='signout-view'),
    path('', IndexView.as_view(), name='index-view'),
]
