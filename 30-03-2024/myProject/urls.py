from django.contrib import admin
from django.urls import path
from myProject.views import candidates, addCandidates, deleteCandi, editCandi, updateCandi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('candidates/', candidates, name='candidates'),
    path('addCandidates/', addCandidates, name='addCandidates'),
    path('deleteCandi/<str:myid>', deleteCandi, name='deleteCandi'),
    path('editCandi/<str:myid>', editCandi, name='editCandi'),

]
