from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('reg', views.registration),
    path('cabinet', views.cabinet, name='cabinet'),
]