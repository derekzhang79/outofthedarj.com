from django.shortcuts import render_to_response
from ootd.students.models import Student
from ootd.links.models import Link

def classes(request):
    student = Student.objects.filter(student_of_the_month__iexact=1)
    return render_to_response('classes.html', {'sotm': student[0]})

def about(request):
    students = Student.objects.filter(ootd_member__iexact=1)
    links = Link.objects.all()
    return render_to_response('about.html', {'students': students,
                                            'links': links})


