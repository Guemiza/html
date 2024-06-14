import uuid
from django.db import models


# Create your models here.
class Author(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, default="")

    date_of_death = models.DateField(null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.last_name


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class BookInstance(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Id Unique")
    due_back = models.DateField(null=True, blank=True)
    book = models.ForeignKey("Book", on_delete=models.SET_NULL, null=True)
    STATUS_CHOICES = [
        ("m", "Maintenance"),
        ("o", "On loan"),
        ("a", "Available"),
        ("r", "Reserved"),
    ]
    imprint = models.CharField(max_length=200, default="0")

    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default="m")

    def __str__(self):
        return self.imprint


class Book(models.Model):
    title = models.CharField(max_length=200, help_text="write a title")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    summary = models.CharField(max_length=200)
    imprint = models.CharField(max_length=200)
    ISBN = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
