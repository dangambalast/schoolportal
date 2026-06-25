from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Student
from django.http import HttpResponse
from django.shortcuts import redirect


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

def login_view(request):
    if request.method == 'POST':

        admission_number = request.POST.get('admission_number')
        try:
            student = Student.objects.get(admission_number=admission_number)
            return render(request, 'fees/dashboard.html', {'student': student}
                          )
        except Student.DoesNotExist:
            return render(request, 'fees/login.html', {"error": 'Student not found!'})

    return render(request, 'fees/login.html')

def logout_view(request):
    return render(request, 'fees/login.html')

def pay_now(request):
    return render(request, 'pay_now.html')