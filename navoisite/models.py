from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    description = models.TextField()
    subjact = models.TextField()

    def __str__(self):
        return self.first_name

