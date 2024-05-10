from django.urls import path
from . import views

urlpatterns = [
    path('searchPatient', views.get_patientData,name='index') , 
    path('UpdatePatientData', views.UpdatePatientData, name='update_patient_data'),

    # other URL patterns...
]
