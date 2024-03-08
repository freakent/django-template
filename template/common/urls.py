from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm

app_name  = 'common'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('signup', views.signup, name = 'signup'),
    path('signin', auth_views.LoginView.as_view(template_name="common/signin.html", authentication_form=LoginForm), name = 'signin'),
]
                             

