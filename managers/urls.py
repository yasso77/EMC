from django.urls import path
from .import views

urlpatterns=[
  path('report',views.check),

]