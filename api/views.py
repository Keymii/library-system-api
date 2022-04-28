from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import library
from .serializer import issuedSerializer, libSerializer, issueSerializer, bookDataSerializer,conciseSerializer

@api_view(['GET']) #home page
def getAll(request):
    books = library.objects.all()
    serializer = libSerializer(books, many=True) #many=True because there will be multiple entities shown
    return Response(serializer.data)

@api_view(['GET']) #issued list
def getIssuedList(request):
    issuedBooks = library.objects.filter(issued=True)
    serializer = issuedSerializer(issuedBooks, many=True)
    return Response(serializer.data)

@api_view(['POST']) #for adding book
def addBook(request): 
    serializer = libSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT']) #for making an issue/returning book
def issueBook(request, pk):
    try: 
        book = library.objects.get(accNo=pk) 
        serializer = issueSerializer(book, data=request.data)
        if serializer.is_valid():
            print('test')
            serializer.save(update_fields=['issued','borrower'])
            return Response(serializer.data)
        else:
            return Response({'message':'something\'s wrong'})
    except library.DoesNotExist: 
        return Response({'message': 'There is no book with accession no. '+str(pk)}) 

@api_view(['GET']) #to get all the info about book
def bookData(request, accno):
    try:
        books = library.objects.get(accNo=accno)
        serializer = bookDataSerializer(books)
        return Response(serializer.data)
    except library.DoesNotExist:
        return Response({'message': 'There is no book with accession no. '+str(accno)}) 

@api_view(['GET']) #for making searches 
def search(request):
    if 'name' in request.query_params:
        name=request.query_params['name']
    else:
        name=""
    if 'author' in request.query_params:
        authName=request.query_params['author']
    else:
        authName=""
    books = library.objects.filter(bookName__icontains=name , author__icontains=authName)
    serializer = conciseSerializer(books, many=True)
    return Response(serializer.data)    

