from django.urls import path
from homepage.views import index, sobrenos, termos

urlpatterns = [
    path('', index),
    path('sobrenos/', sobrenos, name='sobrenos'),
    path('termos/', termos, name='termos'),
]