from django.urls import path
from . import views
urlpatterns = [
    path('employees/',views.EmployeeList.as_view(),name='emplist'),
    path('employees/<int:id>/',views.EmployeeDetails.as_view(),name='empdetails'),
]
