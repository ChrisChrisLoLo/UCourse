from django import forms
from django.forms import widgets
from searchCourse.models import *

SORT_CHOICES = (("name","Name"),("balanced","Balanced Score"))
ASC_CHOICES = (("descending","Descending"),("ascending","Ascending"))
SUBJECT_CHOICES = [("all","All Subjects")]
subject_list = Subject.objects.order_by("letter_code")
for subject_item in subject_list:
    subject_choice = (subject_item.letter_code,subject_item.letter_code+"-"+subject_item.name)
    SUBJECT_CHOICES.append(subject_choice)
class CourseForm(forms.Form):
    sortBy = forms.ChoiceField(label="Sort By",choices=SORT_CHOICES,required=True)
    order = forms.ChoiceField(label="In Order",choices=ASC_CHOICES,required=True)
    subject = forms.ChoiceField(label="Filter By Subject",choices=SUBJECT_CHOICES,required=True)
    courseMin = forms.IntegerField(label="Minimum Course Number",min_value=100,max_value=999,initial=100,required=True)
    courseMax = forms.IntegerField(label="Maximum Course Number",min_value=100,max_value=999,initial=999,required=True)