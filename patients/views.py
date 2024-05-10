from urllib import response
from django.shortcuts import render
from tablib import Dataset

from patients.forms.UploadForm import ExcelUploadForm
from patients.models import Patient
from .resources import PatientsResources
import pandas as pd

import tablib

#from rest_framework import generics


# Create your views here.patientindex
def index(request):
    return render(request,'index.html',{'name':'Yasser'})

def searchPatient(request):

    


    return render(request,'SearchOnPatients.html',{'patients':Patient.objects.all(),'Total':Patient.objects.count()})
    




def upload_excel(request):
    if request.method == 'POST':
            form = ExcelUploadForm(request.POST, request.FILES)      
            excel_file = request.FILES['my_file']
            df = pd.read_excel(excel_file)

            for index, row in df.iterrows():
                Patient.objects.create(
                    fullname=row['Name'],
                    mobile=row['Mobile'],
                    age=row['Age'],
                    sufferedcase=row['Case'],
                    city=row['City'],
                    reservedBy=row['Reserved By'],
                    arrivedOn=row['Arrived On'],
                    remarks=row['Remarks'],
                    expectedDate=row['Arrival Date']

                    # Map other columns accordingly
                )
            return render(request,'form.html',{"status": "Student Data Imported Successfully"})
   
    return render(request, 'uploadPatientData.html', {'form': 'form'})

