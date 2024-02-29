from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, permission_required
from .models import CivilComplaint, EmployeeResponse
from .forms import CivilComplaintForm, EmployeeResponseForm

@login_required
def complaint_list(request):
    complaints = CivilComplaint.objects.filter(user=request.user)
    return render(request, 'complaint_list.html', {'complaints': complaints})

@login_required
def submit_complaint(request):
    if request.method == 'POST':
        form = CivilComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user
            complaint.save()
            return redirect('complaint_list')
    else:
        form = CivilComplaintForm()
    return render(request, 'submit_complaint.html', {'form': form})

@login_required
@permission_required('yourappname.change_civilcomplaint', raise_exception=True)
def respond_to_complaint(request, complaint_id):
    complaint = get_object_or_404(CivilComplaint, pk=complaint_id)
    if request.method == 'POST':
        form = EmployeeResponseForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.complaint = complaint
            response.save()
            complaint.is_resolved = True
            complaint.save()
            return redirect('complaint_list')
    else:
        form = EmployeeResponseForm(initial={'complaint': complaint})
    return render(request, 'respond_to_complaint.html', {'form': form, 'complaint': complaint})
