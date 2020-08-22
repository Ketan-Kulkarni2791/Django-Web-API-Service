from django.urls import path
from .views import employee_list, project_list, employee_detail, project_detail

urlpatterns = [
    path('employee/', employee_list),
    path('employee_detail/<int:emp_id>/', employee_detail),
    path('project/', project_list),
    path('project_detail/<int:project_id>/', project_detail),
]