from django.contrib import admin
from django.urls import path
from myProject.views import student, addStudent
#comment
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', student, name='student'),
    path('addStudent/', addStudent, name='addStudent'),
]
