from django.db import models

class StudentRecord(models.Model):
    name = models.CharField(max_length=100)
    school = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name
