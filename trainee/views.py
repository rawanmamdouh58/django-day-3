from django.shortcuts import render, redirect
from .models import Trainee
from course.models import Course
from django.contrib import messages
from .forms import TraineeForm


def traineeList(request):
    trainees = Trainee.objects.order_by('id')
    courses = Course.objects.filter(status=True)
    return render(request, 'listtrainee.html', {
        "trainees": trainees,
        "courses": courses
    })

def addTrainee(request):
    if request.method == 'POST':
        form = TraineeForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request, 'Trainee added successfully!')

            return redirect('traineeList')
        else:
            return render(request, 'addTrainee.html', {'form': form})

    form = TraineeForm()
    return render(request, 'addTrainee.html', {'form': form})

def updateTrainee(request, id):
    trainee = Trainee.objects.get(id=id)
    if request.method == 'POST':
        selected_course_id = request.POST.get('course')
        course = Course.objects.get(id=selected_course_id) if selected_course_id else None

        Trainee.objects.filter(id=id).update(
            name=request.POST['name'],
            email=request.POST['traineeEmail'],
            image=request.POST['traineeImg'],
            course=course
        )
        return redirect('traineeList')

    courses = Course.objects.filter(status=True)
    return render(request, 'editTrainee.html', {
        "trainee": trainee,
        "courses": courses
    })
def deleteTrainee(request, id):
    Trainee.objects.filter(id=id).update(status=False)
    return redirect('traineeList')