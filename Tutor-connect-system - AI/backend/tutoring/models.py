from django.db import models

class TuitionRequest(models.Model):

    subject = models.CharField(max_length=100)

    location = models.CharField(max_length=100)

    date = models.DateField()

    time = models.TimeField()

    method = models.CharField(max_length=20)

    def __str__(self):
        return self.subject