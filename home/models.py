from django.db import models

class ModelTest(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=15)
    note = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name
