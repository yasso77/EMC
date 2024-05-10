from django.http import JsonResponse
from django.shortcuts import render

from patients.models import PatientVisits

# Create your views here.

def check(request):
    return render(request,'report.html',context={'value':'Yasser'})





