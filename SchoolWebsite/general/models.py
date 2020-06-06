from django.db import models
from django.contrib.auth.models import User, Group

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    information = models.CharField(max_length=500)

class Grade(models.Model):
    LETTERGRADES = (
        ('A', 'Excellent'),
        ('B', 'Good'),
        ('C', 'Average'),
        ('D', 'Poor'),
        ('F', 'Fail')
    )
    value = models.CharField(max_length=1, choices=LETTERGRADES)

class Department(models.Model):
    name = models.CharField(max_length=100)

class DepartmentProfessor(models.Model):
    department = models.ForeignKey(Department, on_delete = models.DO_NOTHING)
    professor = models.ForeignKey(User, limit_choices_to={'groups__name': "Professor"}, on_delete = models.DO_NOTHING)

class Semester(models.Model):
    SEASON = (
        ('FA', 'Fall'),
        ('SP', 'Spring')
    )
    year = models.CharField(max_length = 4)
    type = models.CharField(max_length=4, choices=SEASON)
    regopen = models.BooleanField()

class Course(models.Model):
    name = models.CharField(max_length=100)
    credits = models.IntegerField()
    professor = models.ForeignKey(User, limit_choices_to={'groups__name': "Professor"}, on_delete = models.DO_NOTHING)
    semester = models.ForeignKey(Semester, on_delete=models.DO_NOTHING)

class MemberGrade(models.Model):
    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    semester = models.ForeignKey(Semester, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.DO_NOTHING)
    grade = models.ForeignKey(Grade, on_delete = models.CASCADE, null=True, blank=True)

class MemberInfo(models.Model):

    class RegStatus(models.TextChoices):
        REGISTERED = 'R'
        UNREGISTERED = 'U'

    user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    name = models.CharField(max_length=10)
    registrationstatus = models.CharField(
        max_length=1,
        choices=RegStatus.choices,
        default=RegStatus.UNREGISTERED,
        )
    contactinfo = models.CharField(max_length=20, blank=True)
    email = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)