# Library Management System API

### Overview

This project was created in the year 2022.   
This is a django REST framework based api which allows you to:  
- see all the books in the library  
- add new books to the list  
- issue/return a book     
- check details of a book  
- search for books by book's name and/or author's name  

### Using the API

/admin/ : for admin dashboard

****

`GET ` /

****

Shows a list of all books in the library with their   

- accession number (accNo, integer field, primary key)   
- name (bookName, charfield)   
- author (author, charfield)   
- registration time (regTime, datetime field)   
- issued status (issued, boolean field)   
- if issued, then borrowers name, else empty (borrower, charfield)  

****

`POST` /add/

****

Allows user to add a new book to the database  
Entry in the format:  

    {
        'accNo': some_number,
        'bookName': 'some_book',
        'author': 'some_person'
    }  

The field regTime is auto-filled, field issued=false by default, field borrower="" by default.
Though these fields can also be changed while adding the book  

****

`GET ` /issued/

****

Shows a list of all the issued books with their:  
- accNo
- bookName
- issued (=true)
- borrower  
fields.  

****

`PUT ` /issue/*int*  

****

issue/return page for book with accNo = *int*   

Entry Format:   

    {
        'issued':true/false,
        'borrower': "borrower's name" (keep empty if issued=false)
    }

****

`GET ` /details/*int*

****

shows all the information stored about the book with accNo = *int*

****

`GET ` /search/

****

**keys**: *name* and *author*
shows a list of books having matches with the key's values  

As obvious:  
- *name* key corresponds to book's name
- *author* key corresponds to author's name  

for example

    /search/?name=har&author=rowl

will give a search result with books satisfying:
- name containing "har" and  
- author's name containing "rowl"


### Current status of Database

Right now, database file (db.sqlite3) already stores some data. If you wish to use the API with empty database:
- delete the db.sqlite3 file
- delete the migrations folder present inside the base folder
- then run the following commands on the terminal/command prompt:

    python manage.py makemigrations base
    python manage.py migrate

- then run the server. 
