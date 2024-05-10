from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),   
    path('upload', views.upload_excel,name='push_excel'),
    path('search', views.searchPatient,name='search'),

    # other URL patterns...
]
