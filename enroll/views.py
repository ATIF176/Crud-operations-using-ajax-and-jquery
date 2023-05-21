from django.shortcuts import render
from .forms import StudentRegistration
from .models import User
from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def index(request):
    form = StudentRegistration()
    students = User.objects.all()
    context = {'form':form, 'students':students}
    return render(request, 'enroll/index.html', context)


# @csrf_exempt
def SaveData(request):
    if request.method == "POST":
        form = StudentRegistration(request.POST)
        if form.is_valid():
            sid = request.POST.get('stuid')
            name = request.POST['name']
            email = request.POST['email']
            password = request.POST['password']
            if (sid == ""):
                usr = User(name = name, email = email, password = password)
            else:
                usr = User(id = sid, name = name, email = email, password = password)
            usr.save()
            student = User.objects.values()
            print(student)
            student_data = list(student)
            return JsonResponse({'status':'Save', 'student_data':student_data})
        else:
            return JsonResponse({'status':0})
        
def DeleteData(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)
        user = User.objects.get(pk=id)
        user.delete()
        return JsonResponse({'status':1})
    else:
        return JsonResponse({'status':0})
    context = {}


def EditData(request):
    if request.method == "POST":
        id = request.POST.get('sid')
        print(id)
        student = User.objects.get(pk=id)
        student_data = {"id":student.id, "name":student.name, "email":student.email, "password":student.password}
        return JsonResponse(student_data)

