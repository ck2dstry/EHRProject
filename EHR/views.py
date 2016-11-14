from django.shortcuts import render, render_to_response, redirect
from .models import PatientInfo
from .forms import PostPatientInfoForm
from django.template import RequestContext


def patient_update(request):
    
    if request.method == "POST": 
        
        form = PostPatientInfoForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('patient_list')     
        
    else:
        form = PostPatientInfoForm()

    patients = PatientInfo.objects.all()

    # RequestContext wrapper allows more than one dataset to show on one view, without bitching about the csrf_token.
    return render_to_response('EHR/patient_update.html', RequestContext(request, {'form': form, 'patients': patients}))
    


def patient_list(request):
    return render_to_response('EHR/patient_list.html', {'obj': PatientInfo.objects.all()})
    
    
def visit_update(request):
    return render(request, 'EHR/visit_update.html')
        
    