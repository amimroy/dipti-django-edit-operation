from django.shortcuts import redirect, render
from myApp.models import studentModel
def student(request):
    student=studentModel.objects.all()
    stdDict={
        'std':student
    }
    return render(request, 'student.html', stdDict)

def addStudent(request):
    if request.method=='POST':
        fname=request.POST.get('fname')
        roll=request.POST.get('fname')
        city=request.POST.get('fname')
        student=studentModel(
            FirstName=fname,
            Roll=roll,
            City=city
        )
        student.save()
        return redirect('student')
    return render(request, 'addStudent.html')

