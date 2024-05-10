from logging import NullHandler
from urllib import request
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from doctors.models import Doctor
from patients.models import Patient
from patients.models import PatientVisits
from datetime import datetime
# Create your views here.

def doctorindex(request):
    return render(request,'doc.html',{'name':'Yasser'})

def patientvisit(request):
    return render(request,'PatientVisit.html',{'patients':Patient.objects.all(),'Total':Patient.objects.count()})


def liveReport(request):
    return render(request,'EvaulationReport.html',{'patients':'yasser'})


def addPatientVisit(request):
    txtpatientid=request.POST.get('hdfpatientid')
    doctorid=1 #request.POST.get('doctorid')
    txtdiagnosis=request.POST.get('Diagnosis')
    EvaulDegree=request.POST.get('gridRadios')
    #chkFollowup=request.POST.get('chkFollow')
    EvaulDegree=request.POST.get('gridRadios')
    txtRemarks=request.POST.get('txtRemarks')

    if request.method=='POST':
       # followup = True if chkFollowup == 'on' else False
        patient = Patient.objects.get(pk=txtpatientid)
        doctor = Doctor.objects.get(pk=doctorid)
        data=PatientVisits(patientid=patient,diagnosis=txtdiagnosis,evaluationeegree=EvaulDegree,visitdate=datetime.now(),doctorid=doctor,reasonforvisit=txtRemarks,createdate='2024-04-30')#datetime.now()
        data.save()
        return HttpResponseRedirect("Message")






def ConfirmMsg(request):
     return render(request,'ConfirmMsg.html',{'Msg':request.POST.get('msg')})


def ajaxReportChartEvlDegree(request):
    if request.method == 'POST' and 'inputDate' in request.POST:
            visitdate = request.POST.get('inputDate', None)
            queryset = PatientVisits.objects.filter(createdate='2024-04-30').values('evaluationeegree')    

        # Convert QuerySet to list of dictionaries
            data = list(queryset.values())

        # Return JsonResponse with the converted data
            return JsonResponse(data, safe=False)
            
    else:
            return JsonResponse({'success': False, 'error': 'Invalid request'})  
    

def reportx(request):
    current_time = datetime.now().time()
    return render(request,'report.html',context={'current_time': current_time})
