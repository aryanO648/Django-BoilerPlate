from rest_framework import serializers
from .models import User, Book, BookDetails, BorrowedBooks

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'membership_date']

class BookDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookDetails
        fields = ['id', 'number_of_pages', 'publisher', 'language']

class BookSerializer(serializers.ModelSerializer):
    details = BookDetailsSerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'isbn', 'published_date', 'genre', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details')
        book = Book.objects.create(**validated_data)
        BookDetails.objects.create(book=book, **details_data)
        return book

    def update(self, instance, validated_data):
        details_data = validated_data.pop('details')
        instance.title = validated_data.get('title', instance.title)
        instance.isbn = validated_data.get('isbn', instance.isbn)
        instance.published_date = validated_data.get('published_date', instance.published_date)
        instance.genre = validated_data.get('genre', instance.genre)
        instance.save()

        details_instance = instance.details
        details_instance.number_of_pages = details_data.get('number_of_pages', details_instance.number_of_pages)
        details_instance.publisher = details_data.get('publisher', details_instance.publisher)
        details_instance.language = details_data.get('language', details_instance.language)
        details_instance.save()

        return instance

class BorrowedBooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BorrowedBooks
        fields = ['id', 'user', 'book', 'borrow_date', 'return_date']
