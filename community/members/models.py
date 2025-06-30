from django.db import models
from library.models import Book

class Member(models.Model):
    name = models.CharField(max_length=100)
    borrowed_book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
