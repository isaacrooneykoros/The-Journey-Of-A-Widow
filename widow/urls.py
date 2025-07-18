# from django.contrib import admin
from django.urls import path, include

from widow import views

urlpatterns = [
    #    path('admin/', admin.site.urls),
path('', views.index, name='index'),
]
