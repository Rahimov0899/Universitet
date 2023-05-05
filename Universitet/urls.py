from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ustozlar/', ustozlar),
    path('bitta_ochir/<int:id>/', ustoz),
    path('fanlar/', fanlar),
    path('bitta_ochir/<int:id>/', fan),
    path('yonalish/', yonalishlar),
    path('bitta_ochir/<int:id>/', yonalish),
]
