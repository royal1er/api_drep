from django.db import models

class Language(models.Model):
    question = models.CharField(max_length=100)
    a = models.CharField(max_length=50)
    b = models.CharField(max_length=50)
    c = models.CharField(max_length=50)
    d = models.CharField(max_length=50)

    def __str__(self):
        return self.question
