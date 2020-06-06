from django import forms
from general.models import MemberInfo, MemberGrade, Grade
from django.contrib.auth.models import User

REGSTATUS = [
    ('REGISTERED', 'REGISTERED'),
    ('UNREGISTERED', 'UNREGISTERED')
]

class StudentInfoForm(forms.ModelForm):
    class Meta:
        model = MemberInfo
        fields = ['contactinfo', 'email', 'phone','address']

class SignupStudentForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

class GradeEditForm(forms.Form):
    class Meta:
        model = MemberGrade
        fields = ['grade']

class RegCoursesForm(forms.ModelForm):
    class Meta:
        model = MemberGrade
        fields = ['user', 'semester', 'course', 'grade']