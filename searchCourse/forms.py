from django import forms
from django.forms import widgets, ModelForm
from searchCourse.models import *

SORT_CHOICES = (("name","Name"),("balanced","Balanced Score"),("difficulty","Difficulty Score"),("workload","Workload Score"),("practicality","Practicality Score"),("enjoyment","Enjoyment Score"),("weighted","Weighted Score"))
ASC_CHOICES = (("descending","Descending"),("ascending","Ascending"))
SUBJECT_CHOICES = [("all","All Subjects")]
subject_list = Subject.objects.order_by("letter_code")
for subject_item in subject_list:
    subject_choice = (subject_item.letter_code,subject_item.letter_code+"-"+subject_item.name)
    SUBJECT_CHOICES.append(subject_choice)
LEVEL_CHOICES = ((100,"100"),(200,"200"),(300,"300"),(400,"400"),(500,"500"),(600,"600"),(700,"700"),(800,"800"),(900,"900"),(1000,"1000"))

class CourseForm(forms.Form):
    sortBy = forms.ChoiceField(label="Sort By",choices=SORT_CHOICES,required=True,initial=SORT_CHOICES[0])
    order = forms.ChoiceField(label="In Order",choices=ASC_CHOICES,required=True,initial=SORT_CHOICES[0])
    subject = forms.ChoiceField(label="Filter By Subject",choices=SUBJECT_CHOICES,required=True,initial=SUBJECT_CHOICES[0])
    courseMin = forms.ChoiceField(label="Minimum Course Number",choices=LEVEL_CHOICES,required=True,initial=LEVEL_CHOICES[0])
    courseMax = forms.ChoiceField(label="Maximum Course Number",choices=LEVEL_CHOICES,required=True,initial=LEVEL_CHOICES[2])

class RatingForm(forms.Form):
    diffScore = forms.IntegerField(label="How easy was the course?",min_value=1,max_value=5,required=True,initial=0)
    workScore = forms.IntegerField(label="How nice was the workload for the course?",min_value=1,max_value=5,required=True,initial=0)
    pracScore = forms.IntegerField(label="How practical was the course?",min_value=1,max_value=5,required=True,initial=0)
    enjoyScore = forms.IntegerField(label="How enjoyable was the course?",min_value=1,max_value=5,required=True,initial=0)
    comment = forms.CharField(label="Additional comments (Optional)",widget=forms.Textarea,max_length=400,required=False)
    #gpa = forms.DecimalField(label="Average class GPA (Optional)",min_value=0,max_value=4,required=False)

# class RateForm(ModelForm):
#     class Meta:
#         model = Rating
#         fields = ["difficulty_score","workload_score","practicality_score","enjoyment_score"]
