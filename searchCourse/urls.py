from django.urls import path

from . import views

app_name = 'courseSearch'
urlpatterns = [
    path('', views.index, name='index'),
    #path('<str:subject_id>',views.subject, name='subject'),
    path('<str:subject_id>/<int:course_id>',views.detail, name='detail'),
    path('<str:subject_id>/<int:course_id>/rate',views.rate, name='rate'),
    path('success',views.success,name='rate_success'),
]
