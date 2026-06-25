from django.shortcuts import render
from .models import Student
from django.urls import path
from .import views
from .views import login_view, pay_now, logout_view


urlpatterns = [
    path('pay/', pay_now, name='pay'),
    path('login/', login_view, name="login"),
    path('login/', views.login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('pay-now/', pay_now, name="pay_now"),

]
def login_view(request):
    if request.method == 'POST':

        admission_number = request.POST.get('admission_number')
        try:
            student = Student.objects.get(admission_number=admission_number)
            return render(request, 'fees/dashboard.html', {'student': student}
                          )
        except Student.DoesNotExist:
            return render(request, 'fees/login.html, {"error": Student not found!"})')

    return render(request, 'fees/login.html')