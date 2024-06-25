from django.urls import path
from homepage.views import login, logout
from registro.views import registro, dashboard

urlpatterns = [
    path('registro/', registro, name='registro'),
    path('login/', login, name='login'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout, name='logout'),
]