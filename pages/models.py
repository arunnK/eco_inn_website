from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name  = models.CharField(max_length=30)
    roll_no = models.CharField(max_length=10)
    mob_no = models.CharField(max_length=13)
    branch = models.CharField(max_length=30)
    message = models.CharField(max_length=200)
    email = models.EmailField()

#class problem_bank(models.Model):
