# from django.urls import path, include
# from . import views


# urlpatterns = [
#     # path('login/', views.login, name='login'),
#     # path('signup/', views.signup, name='signup')
#     path('', views.index, name='index'),
#     path('login/', views.login, name='login'),
#     path('signup/', views.signup, name='signup')
# ]

from django.urls import path, include
from . import views

app_name  = 'authentication'

urlpatterns = [
   
    path('', views.index , name='index'),
    path('signup/', views.signup , name='signup'),
    path('login/', views.login , name='login'),
    path('logout/', views.logout , name='logout'),
]