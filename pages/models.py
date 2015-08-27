from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)
    roll_no = models.CharField(max_length=10)
    mob_no = models.CharField(max_length=13)
    branch = models.CharField(max_length=30)
    message = models.CharField(max_length=500)
    email = models.EmailField()

class ProblemBank(models.Model):
    problem_statement = models.CharField(max_length=5000)
    submitted_by = models.CharField(max_length=60)
    mob_no =  models.CharField(max_length=13)
    email = models.EmailField()
