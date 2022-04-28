from django.db import models

class library(models.Model):
    accNo = models.IntegerField( primary_key=True)  #accession number (primary key)
    bookName = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    regTime = models.DateTimeField(auto_now_add=True)  #updates only at the time of entry of the book
    issued = models.BooleanField(default=False)
    borrower = models.CharField(max_length=200, default="", blank=True)
    last_issue_update = models.DateTimeField(auto_now=True, blank=True) #updates everytime issue status is changed

