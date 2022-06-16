from django.db import models

# Create your models here.
class PersonFolio(models.Model):
    fName = models.CharField(max_length=20)
    lName = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)

    #education = models.CharField(max_length=40)

    #skills = []

    #projects = []
    prjName = models.CharField(max_length=20)


class CommaSepField(models.CharField):
    
    def __init__(self, separator=",", *args, **kwargs):
        self.separator = separator
        super().__init__(*args, **kwargs)


class Project(models.Model):
    name = models.CharField(max_length=20)
    picture = models.CharField(max_length=20) #CHANGE TO FILE

class Skill(models.Model):
    skill = models.CharField(max_length=20)

