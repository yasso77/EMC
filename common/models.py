from django.db import models
from django.http import JsonResponse

from patients.models import Patient

# Create your models here.

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


