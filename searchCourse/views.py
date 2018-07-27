from django.shortcuts import render
from django.http import HttpResponse
from searchCourse.models import *

def index(request):
    subject_list = Subject.objects.order_by("letter_code")
    course_list = Course.objects.order_by("name")[:20]
    #print(course_list)
    context = {"subject_list":subject_list,
                "course_list":course_list}
    return render(request,"searchCourse/index.html",context)

# def subject(request, subject_id):
#     return HttpResponse("You're looking at subject {}.".format(subject_id))

def detail(request, subject_id, course_id):
    subject_id = subject_id.upper()
    select_subject = Subject.objects.get(letter_code=subject_id)
    select_course = Course.objects.get(number_code=course_id,subject=select_subject.id)
    #print(select_course)
    context = {"course":select_course,
                "subject":select_subject}
    return render(request,"searchCourse/detail.html",context)
    #return HttpResponse("You're looking at course {} {}.".format(subject_id,course_id))

def rate(request, subject_id, course_id):
    return HttpResponse("You're rating the course {} {}.".format(subject_id,course_id))