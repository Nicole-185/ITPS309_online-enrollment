from django.db import models
 
class StudentInfo(models.Model):
    name = models.CharField(max_length=100)
    studid = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    def  __str__(self):
        return f"{self.name}"
    
class EducationalBackground(models.Model):
    level = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    year = models.IntegerField()
    attainment = models.CharField(max_length=100)

    def  __str__(self):
        return f"{self.school}"
    
class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    studid = models.CharField(max_length=100)
    cpno = models.IntegerField()

    def  __str__(self):
        return f"{self.username}"
    
class FamilyBackground(models.Model):
    name = models.CharField(max_length=100)
    occupation = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits= 8 , decimal_places= 2)
    address = models.CharField(max_length=100)
    cpno = models.CharField(max_length=100)

    def  __str__(self):
        return f"{self.name}"
    
class Subjects(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    units = models.IntegerField()
    schedule = models.CharField(max_length=100)
    inst = models.CharField(max_length=100)

    def  __str__(self):
        return f"{self.code}"