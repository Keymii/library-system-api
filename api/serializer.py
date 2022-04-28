from modulefinder import IMPORT_NAME
from rest_framework import serializers
from base.models import library

class libSerializer (serializers.ModelSerializer): #for home page
    class Meta:
        model=library
        fields=['accNo','bookName','author','regTime', 'issued', 'borrower']

class issuedSerializer (serializers.ModelSerializer): #for issued list page
    class Meta:
        model=library
        fields= ['accNo','bookName', 'issued', 'borrower','last_issue_update']

class issueSerializer (serializers.ModelSerializer): #for issue/return page
    class Meta:
        model=library
        fields= ['issued', 'borrower']

class bookDataSerializer (serializers.ModelSerializer): #all details of the book
    class Meta:
        model=library
        fields= '__all__'

class conciseSerializer (serializers.ModelSerializer): #for searches
    class Meta:
        model=library
        fields= ['accNo','bookName','author','issued']