from django.shortcuts import render
from django.http import HttpResponse
from searchCourse.models import *

def index(request):
    subject_list = Subject.objects.order_by('letter_code')
    course_list = Course.objects.order_by('name')[:20]
    print(course_list)
    context = {'subject_list':subject_list,
                'course_list':course_list}
    return render(request,"searchCourse/index.html",context)

# def subject(request, subject_id):
#     return HttpResponse("You're looking at subject {}.".format(subject_id))

def detail(request, subject_id, course_id):
    return HttpResponse("You're looking at course {} {}.".format(subject_id,course_id))

def rate(request, subject_id, course_id):
    return HttpResponse("You're rating the course {} {}.".format(subject_id,course_id))