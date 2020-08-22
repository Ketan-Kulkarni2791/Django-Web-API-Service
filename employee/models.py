from django.db import models


class Employee(models.Model):
    emp_id = models.IntegerField(primary_key=True)
    lastname = models.CharField(max_length=100)
    firstname = models.CharField(max_length=100)
    join_date = models.DateField(auto_now_add=True)
    email = models.EmailField(max_length=100)
    isActive = models.BooleanField(default=False)

    def __str__(self):
        return self.firstname


class Projects(models.Model):
    project_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(auto_now=True)
    isActive = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class EmpProject(models.Model):
    emp_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)

    def __str__(self):
        return self.emp_id
