from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render
from django.http import HttpResponse

from searchCourse.models import *
from .forms import CourseForm
DEF_SEARCH_PARAMS = {"sortBy":"name","order":"descending","subject":"all","courseMin":100,"courseMax":999}

def index(request):
    
    #Cannot find a way to get initial field values from forms.py
    #Using DEF_SEARCH_PARAMS works but violates DRY,
    #need to find a way to work around it.

    form = CourseForm(DEF_SEARCH_PARAMS)
    search_params = form.data

    #subject_list = Subject.objects.order_by("letter_code")
    #course_list = Course.objects.order_by("name")

    if request.GET:
        get_form = CourseForm(request.GET)
        if get_form.is_valid():
            form = get_form
            search_params = form.cleaned_data

    if search_params["order"] == "descending":
        asc_char = "-"
    elif search_params["order"] == "ascending":
        asc_char = ""

    search_courses = Course.objects.order_by(asc_char+search_params["sortBy"])
    search_courses = search_courses.filter(
                    number_code__gte = int(search_params["courseMin"]),
                    number_code__lte = int(search_params["courseMax"]),
                    )

    if search_params["subject"] != "all":
        search_courses = search_courses.filter(
                        subject__letter_code = search_params["subject"]
                        )
    

    search_paginator = Paginator(search_courses,15)
    page = request.GET.get("page")
    found_courses = search_paginator.get_page(page)

    context = {
                "search_list":found_courses,
                "form":form,
            }
    return render(request,"searchCourse/index.html",context)

# def subject(request, subject_id):
#     return HttpResponse("You're looking at subject {}.".format(subject_id))

def detail(request, subject_id, course_id):
    subject_id = subject_id.upper()
    select_subject = Subject.objects.get(letter_code=subject_id)
    select_course = Course.objects.get(number_code=course_id,subject=select_subject.id)
    #print(select_course)

    form = CourseForm(request.GET)
    if not form.is_valid():
        form = CourseForm(DEF_SEARCH_PARAMS)
        
    context = {"course":select_course,
                "subject":select_subject,
                "form":form}
    return render(request,"searchCourse/detail.html",context)
    #return HttpResponse("You're looking at course {} {}.".format(subject_id,course_id))

def rate(request, subject_id, course_id):
    
    form = 1
    context = {"form":form,}
    return render(request,"accounts/sign_up.html",context)
