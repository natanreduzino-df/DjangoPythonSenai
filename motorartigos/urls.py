from django.urls import path 
from motorartigos.views import index, artigo

urlpatterns = [
    path('', index, name='home'), 
    path('artigos/', index, name='index'), 
    path('artigo/<int:id>/', artigo, name='artigo'),
]
