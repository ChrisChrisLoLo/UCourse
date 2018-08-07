from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render,redirect
from django.http import HttpResponse

from searchCourse.models import *
from .forms import CourseForm, RatingForm
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
    if request.method == "POST":
        form = RatingForm(request.POST)
        if form.is_valid():
            #validate subject/course id
            subject_id = subject_id.upper()
            select_subject = Subject.objects.get(letter_code=subject_id)
            select_course = Course.objects.get(number_code=course_id,subject=select_subject.id)

            if select_course:
                if not request.user.is_authenticated:
                    return redirect("/accounts/login")
                diff_score = form.cleaned_data.get("diffScore")
                work_score = form.cleaned_data.get("workScore")
                prac_score = form.cleaned_data.get("pracScore")
                enjoy_score = form.cleaned_data.get("enjoyScore")
                comment = form.cleaned_data.get("comment")
                #Create rating form or update it if user has already created one.
                #Rating is the object updated or created, created is a boolean 
                rating, was_created = Rating.objects.update_or_create(
                    course = select_course,
                    user = request.user,
                    defaults = {
                        "difficulty_score":diff_score,
                        "workload_score":work_score,
                        "practicality_score":prac_score,
                        "enjoyment_score":enjoy_score,
                        "comment":comment
                    }
                )
                return redirect("/search/success")
            else:
                #Raise error indincating no course found
                pass
            
    else:
        form = RatingForm()

    context = {"form":form,
                "course_id":course_id,
                "subject_id":subject_id}
    return render(request,"searchCourse/rate_form.html",context)


def success(request):
    return render(request,"searchCourse/success.html")