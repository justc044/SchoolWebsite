from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('displayinfo/<int:pk>', views.displayinfo, name='displayinfo'),
    path('editinfo/<int:pk>', views.editinfo, name='editinfo'),
    path('edit/<int:pk>', views.studentinfoedit, name='studentinfoedit'),
    path('displaygrades/<int:pk>', views.displaygrades, name='displaygrades'),
    path('managegrades/<int:pk>', views.managegrades, name='managegrades'),
    path('editgrades/<int:upk>/<int:pk>', views.editgrades, name='editgrades'),
    path('editgrade/<int:upk>/<int:pk>', views.editgrade, name='editgrade'),
    path('regcourses/<int:upk>', views.regcourses, name='regcourses'),
    path('registercourses/<int:upk>', views.registercourses, name='registercourses'),
    path('courses/<int:upk>', views.courses, name='courses'),
    path('submitgrade/<int:pk>/<int:upk>', views.submitgrade, name='submitgrade'),
]

