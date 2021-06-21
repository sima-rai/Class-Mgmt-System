from django.db import models
from django.contrib.auth.models import User
from .constants import *

# Create your models here.

class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS)

    class Meta:
        abstract = True


class School(TimeStamp):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Grade(TimeStamp):
    grade = models.CharField(max_length=100)

    def __str__(self):
        return self.grade

class Teacher(TimeStamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name


class Student(TimeStamp):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    contact = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

