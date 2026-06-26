from django.contrib import admin
from django.urls import path,include
import motorartigos
from motorartigos.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('motorartigos.urls')), 
]




