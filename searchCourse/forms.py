from django import forms
from django.forms import widgets
from searchCourse.models import *

SORT_CHOICES = (("name","Name"),("balanced","Balanced Score"),("difficulty","Difficulty Score"),("workload","Workload Score"),("practicality","Practicality Score"),("enjoyment","Enjoyment Score"),("weighted","Weighted Score"))
ASC_CHOICES = (("descending","Descending"),("ascending","Ascending"))
SUBJECT_CHOICES = [("all","All Subjects")]
subject_list = Subject.objects.order_by("letter_code")
for subject_item in subject_list:
    subject_choice = (subject_item.letter_code,subject_item.letter_code+"-"+subject_item.name)
    SUBJECT_CHOICES.append(subject_choice)


class CourseForm(forms.Form):
    sortBy = forms.ChoiceField(label="Sort By",choices=SORT_CHOICES,required=True,initial=SORT_CHOICES[0])
    order = forms.ChoiceField(label="In Order",choices=ASC_CHOICES,required=True,initial=SORT_CHOICES[0])
    subject = forms.ChoiceField(label="Filter By Subject",choices=SUBJECT_CHOICES,required=True,initial=SUBJECT_CHOICES[0])
    courseMin = forms.IntegerField(label="Minimum Course Number",min_value=100,max_value=999,required=True,initial=100)
    courseMax = forms.IntegerField(label="Maximum Course Number",min_value=100,max_value=999,required=True,initial=999)

#class RateForm(form.Form):