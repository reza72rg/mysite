from django.urls import path
#from accounts.views import *
from . import views 

app_name = 'accounts'

urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('singup/',views.singup_view,name='singup'),
]