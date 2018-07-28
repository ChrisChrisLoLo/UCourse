from django.shortcuts import render
from django.http import HttpResponse
from searchCourse.models import *

DEF_SEARCH_PARAMS = {}

def index(request):
    print(request.GET)
    subject_list = Subject.objects.order_by("letter_code")
    course_list = Course.objects.order_by("name")[:20]
    #ASSUME GET PARAMS ALWAYS FULL
    if not request.GET:
        context = {"subject_list":subject_list,
                "course_list":course_list}
        return render(request,"searchCourse/index.html",context)

    if request.GET["scoreOrder"] == "descending":
        asc_char = "-"
    elif request.GET["scoreOrder"] == "ascending":
        asc_char = ""
    #THROW ERROR OTHERWISE

    search_courses = Course.objects.order_by(asc_char+request.GET["score"])
    search_courses = search_courses.filter(
                    number_code__gte = int(request.GET["courseMin"]),
                    number_code__lte = int(request.GET["courseMax"]),
                    )


    if request.GET["subject"] != "all":
        #search_subject = Subject.objects.get(letter_code= request.GET["subject"])
        search_courses = search_courses.filter(
                        subject__letter_code = request.GET["subject"]
                        )
    

    search_courses = search_courses[:20]

    print(search_courses)

    context = {"subject_list":subject_list,
                "course_list":course_list,
                "search_list":search_courses,
            }
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