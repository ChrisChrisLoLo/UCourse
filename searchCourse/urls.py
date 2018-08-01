from django.urls import path

from . import views

app_name = 'courseSearch'
urlpatterns = [
    path('', views.index, name='search:index'),
    #path('<str:subject_id>',views.subject, name='subject'),
    path('<str:subject_id>/<int:course_id>',views.detail, name='search:detail'),
    path('<str:subject_id>/<int:course_id>/rate',views.rate, name='search:rate'),
]