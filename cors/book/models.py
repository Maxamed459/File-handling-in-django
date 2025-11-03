from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="books/")

    def __str__(self):
        return self.name
    
    def delete(self):
        self.image.delete()
        super().delete()