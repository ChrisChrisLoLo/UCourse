from django.contrib import admin

# Register your models here.
from .models import Faculty
admin.site.register(Faculty)
from .models import Subject
admin.site.register(Subject)
from .models import Course
admin.site.register(Course)
from .models import Rating
admin.site.register(Rating)
