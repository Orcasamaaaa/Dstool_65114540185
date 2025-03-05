from django.db import models

class Course(models.Model):
    Course_id = models.CharField(max_length=10, primary_key=True)
    Course_name = models.CharField(max_length=255)
    Teacher_name = models.CharField(max_length=255)

    def __str__(self):
        return self.Course_name
