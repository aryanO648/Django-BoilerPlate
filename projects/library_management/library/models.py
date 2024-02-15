from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    membership_date = models.DateField()

class Book(models.Model):
    title = models.CharField(max_length=100)
    isbn = models.CharField(max_length=20)
    published_date = models.DateField()
    genre = models.CharField(max_length=50)

class BookDetails(models.Model):
    book = models.OneToOneField(Book, on_delete=models.CASCADE, related_name='details')
    number_of_pages = models.IntegerField()
    publisher = models.CharField(max_length=100)
    language = models.CharField(max_length=50)

class BorrowedBooks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='borrowed_books')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='borrowed_books')
    borrow_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
