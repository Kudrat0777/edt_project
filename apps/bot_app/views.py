from django.shortcuts import render, redirect
from .models import CivilComplaint, EmployeeResponse
from .forms import CivilComplaintForm, EmployeeResponseForm

def complaint_list(request):
    complaints = CivilComplaint.objects.all()
    return render(request, 'complaint_list.html', {'complaints': complaints})

def submit_complaint(request):
    if request.method == 'POST':
        form = CivilComplaintForm(request.POST)
        if form.is_valid():
            complaint = form.save(commit=False)
            complaint.user = request.user  # Привязываем обращение к текущему пользователю
            complaint.save()
            return redirect('complaint_list')
    else:
        form = CivilComplaintForm()

    return render(request, 'submit_complaint.html', {'form': form})

def respond_to_complaint(request, complaint_id):
    complaint = CivilComplaint.objects.get(pk=complaint_id)

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
        form = EmployeeResponseForm()

    return render(request, 'respond_to_complaint.html', {'form': form, 'complaint': complaint})
