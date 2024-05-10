from django.http import JsonResponse
from django.shortcuts import render

from patients.models import Patient

# Create your views here.

# Called by AJAX request
def get_patientData(request):

    if request.method == 'POST' and 'myData' in request.POST:
        patientID = request.POST.get('myData', None)
        queryset = Patient.objects.filter(patientid=patientID)    

    # Convert QuerySet to list of dictionaries
        data = list(queryset.values())

    # Return JsonResponse with the converted data
        return JsonResponse(data, safe=False)
        
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request'})  
    

def UpdatePatientData(request):
    if request.method == 'POST':
        patientAge=request.POST.get('txtAge')
        patient_id = request.POST.get('hdfpatientid')
       

         # Retrieve the patient object
        try:
            patient = Patient.objects.get(patientid=patient_id)
        except Patient.DoesNotExist:
            return JsonResponse({'error': 'Patient not found'}, status=404)

        # Update patient attributes
        patient.age = patientAge

        # Save the updated patient object
        patient.save()

        return render(request,"ConfirmMsg.html",{'message': 'Patient data updated','returnUrl':'search'}, status=200)
   # return render(request,"/patient/templates/SearchOnPatients.html",{'message': 'Error','returnUrl':'/patient/search'}, status=404)



