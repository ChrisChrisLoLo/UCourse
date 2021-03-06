from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Avg, F
#TODO somehow ensure that searchCourse.models is not imported in the case that a db is not initialized.
from searchCourse.models import *
from .forms import CourseForm, RatingForm
DEF_SEARCH_PARAMS = {"sortBy":"name","order":"descending","subject":"all","courseMin":100,"courseMax":1000}
CRITERION_NUM = 4


def index(request):
    
    #Cannot find a way to get initial field values from forms.py
    #Using DEF_SEARCH_PARAMS works but violates DRY,
    #need to find a way to work around it.

    form = CourseForm(DEF_SEARCH_PARAMS)
    search_params = form.data

    if request.GET:
        get_form = CourseForm(request.GET)
        if get_form.is_valid():
            form = get_form
            search_params = form.cleaned_data

    if search_params["order"] == "descending":
        asc_char = "-"
    elif search_params["order"] == "ascending":
        asc_char = ""
    
    search_courses = Course.objects.filter(
                    number_code__gte = int(search_params["courseMin"]),
                    number_code__lte = int(search_params["courseMax"]),
                    )

    if search_params["subject"] != "all":
        search_courses = search_courses.filter(
                        subject__letter_code = search_params["subject"]
                        )

    #Query is unoptimized since it is finding each score twice rather than finding it once.
    #I do not know how to work around this with Django's ORM.
    search_courses = search_courses.annotate(difficulty=Avg("rating__difficulty_score"))\
                                    .annotate(workload=Avg("rating__workload_score"))\
                                    .annotate(practicality=Avg("rating__practicality_score"))\
                                    .annotate(enjoyment=Avg("rating__enjoyment_score"))\
                                    .annotate(balanced=((Avg("rating__difficulty_score")+Avg("rating__workload_score")+Avg("rating__practicality_score")+Avg("rating__enjoyment_score"))/CRITERION_NUM))\
                                    .order_by(asc_char+search_params["sortBy"])
    
    #search_courses = Course.objects.order_by(asc_char+search_params["sortBy"])

    
    

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

#TODO: MECE somehow lost the space when it went from the webpage to the csv. Need to make change to csv to fix this

def detail(request, subject_id, course_id):
    subject_id = subject_id.upper()
    select_subject = Subject.objects.get(letter_code=subject_id)

    select_course = Course.objects  .annotate(difficulty=Avg("rating__difficulty_score"))\
                                    .annotate(workload=Avg("rating__workload_score"))\
                                    .annotate(practicality=Avg("rating__practicality_score"))\
                                    .annotate(enjoyment=Avg("rating__enjoyment_score"))\
                                    .annotate(balanced=((Avg("rating__difficulty_score")+Avg("rating__workload_score")+Avg("rating__practicality_score")+Avg("rating__enjoyment_score"))/CRITERION_NUM))\
                                    .get(number_code=course_id,subject=select_subject.id)\

    select_ratings = Rating.objects .annotate(username = F("user__username"))\
                                    .filter(course=select_course)

    #Fills in form from previous page is possible
    form = CourseForm(request.GET)
    if not form.is_valid():
        form = CourseForm(DEF_SEARCH_PARAMS)
        
    context = {"course":select_course,
                "subject":select_subject,
                "ratings":select_ratings,
                "form":form}
    return render(request,"searchCourse/detail.html",context)

def rate(request, subject_id, course_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = RatingForm(request.POST)
            if form.is_valid():
                #validate subject/course id
                subject_id = subject_id.upper()
                select_subject = Subject.objects.get(letter_code=subject_id)
                select_course = Course.objects.get(number_code=course_id,subject=select_subject.id)

                if select_course:
                    
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
                    #Raise error indicating no course found
                    pass
                
        else:
            form = RatingForm()

        context = {"form":form,
                    "course_id":course_id,
                    "subject_id":subject_id}
        return render(request,"searchCourse/rate_form.html",context)
    #Redirect if not authenticated
    return redirect("/accounts/login")


def success(request):
    return render(request,"searchCourse/success.html")