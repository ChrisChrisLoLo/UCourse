from django.db import models

# Create your models here.
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
        return self.letter_code+' - '+self.name
        
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