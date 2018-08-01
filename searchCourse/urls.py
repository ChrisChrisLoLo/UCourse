from django.urls import path

from . import views

app_name = 'courseSearch'
urlpatterns = [
    path('', views.index, name='courseSearch:index'),
    #path('<str:subject_id>',views.subject, name='subject'),
    path('<str:subject_id>/<int:course_id>',views.detail, name='courseSearch:detail'),
    path('<str:subject_id>/<int:course_id>/rate',views.rate, name='courseSearch:rate'),
]