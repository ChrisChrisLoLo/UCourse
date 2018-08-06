from django.core.validators import MinValueValidator,MaxValueValidator

from django.db import models
from django.contrib.auth.models import User


class Faculty(models.Model):
    name = models.CharField(max_length=60)
    def __str__(self):
        return self.name

class Subject(models.Model):
    faculty = models.ForeignKey(
        Faculty,
        on_delete=models.CASCADE,
        )
    name = models.CharField(max_length=120)
    letter_code = models.CharField(max_length=6)
    def __str__(self):
        return self.letter_code+" - "+self.name
        
class Course(models.Model):
    subject = models.ForeignKey(
        Subject,
        on_delete=models.CASCADE,
    )
    number_code = models.PositiveSmallIntegerField()
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=1600)
    def __str__(self):
        return self.name

class Rating(models.Model):
    course = models.ForeignKey(
        Course,
        null = True,
        on_delete=models.SET_NULL, #Do not destroy user ratings in case of a hiccup.
    )
    user = models.ForeignKey(
        User,
        null = True,
        on_delete=models.SET_NULL
    )
    difficulty_score = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    workload_score = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    practicality_score = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    enjoyment_score = models.PositiveSmallIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ]
    )
    comment = models.CharField(max_length=400, blank=True, null=True)
    gpa = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        validators=[
            MaxValueValidator(4),
            MinValueValidator(0)
        ],
        null=True
    )
