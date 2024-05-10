from django.urls import path
from . import views

urlpatterns = [
   
    path('about', views.doctorindex,name='aboutDOC'),
    path('newvisit', views.patientvisit,name='newvisit'),   
    path('report',views.ajaxReportChartEvlDegree,name='LiveEvulationReport'),
     path('reportPagex',views.reportx,name='reportPagex'),    
    path('AddVisit',views.addPatientVisit,name='SubmitVisit'),
    path('Message',views.ConfirmMsg,name='MessageAlert'),

    # other URL patterns...
]
