from django.urls import path
from . import views

urlpatterns=[
    path('',views.getAll),
    path('add/',views.addBook),
    path('issued/',views.getIssuedList),
    path('issue/<int:pk>',views.issueBook),
    path('details/<int:accno>',views.bookData),
    path('search/',views.search),
    
]