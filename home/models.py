from django.db import models


class ContactModel(models.Model):
    sno = models.AutoField(primary_key=True)
    fullName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    msg = models.TextField()

    def __str__(self):
        return self.fullName


class ProjectModel(models.Model):
    sNo = models.AutoField(primary_key=True)
    projectName = models.CharField(max_length=100)
    frontEnd = models.CharField(max_length=100)
    backEnd = models.CharField(max_length=100)
    database = models.CharField(max_length=100)
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.projectName
