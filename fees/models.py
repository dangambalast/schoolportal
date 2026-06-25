from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    admission_number = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=128, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    student_class = models.CharField(max_length=20, null=True, blank=True)
    school_fees = models.IntegerField()
    paid = models.BooleanField(default=False)
    passport = models.ImageField(upload_to="passports/", null=True, blank=True)



    def __str__(self):
        return self.name
