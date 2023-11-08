import uuid
from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    date_of_death = models.DateField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class BookInstance(models.Model):

    uniqueId =models.UUIDField(primary_key=True,
                                   default=uuid.uuid4, help_text='Id Unique')
    due_back= models.DateField(null=True,blank=True)
    book = models.ForeignKey('Book',on_delete=models.SET_NULL, null=True)
    LOAN_STATUS = (
            ('m','Maintenance'),
            ('o','On loan'),
            ('a', 'Available'),
            ('r', 'Reserved'),
        )

    def __str__(self):
        return self.book
class Book(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE,null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    title =models.CharField(max_length=200, help_text='write a title')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary =models.CharField(max_length=200)
    imprint =models.CharField(max_length=200)
    ISBN =models.CharField(max_length=200)




    def __str__(self):
        return self.title




