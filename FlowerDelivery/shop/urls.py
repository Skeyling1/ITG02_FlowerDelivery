from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('reg/', views.register, name='register'),
    path('cabinet', views.cabinet, name='cabinet'),
]