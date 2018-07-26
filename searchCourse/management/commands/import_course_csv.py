import csv

from django.core.management.base import BaseCommand, CommandError
from searchCourse.models import Faculty, Subject, Course

class Command(BaseCommand):
    help = 'Imports a custom CSV of all the Course information and creates/updates the data'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)
    
    def handle(self, *args, **options):
        print("Running... Please be patient")
        with open('./scriptResources/UAlbertaCoursesSingleTable.csv', newline='') as csvFile:
            csvReader = csv.reader(csvFile)
            #Skip first row (the title row)
            next(csvReader)
            for row in csvReader:
                #Note: Obj is the resulting entry created as an object
                #Created is a boolean.
                facultyObj, facultyCreated = Faculty.objects.get_or_create(
                    name=row[0],
                )
                subjectObj, subjectCreated = Subject.objects.get_or_create(
                    name=row[1],
                    letter_code=row[2],
                    faculty=facultyObj
                )
                courseObj, courseCreated = Course.objects.get_or_create(
                    number_code=row[3],
                    name=row[4],
                    description=row[5],
                    subject=subjectObj
                )