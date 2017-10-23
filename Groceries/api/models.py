from django.db import models

# Create your models here.
class Grocerylist(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=False)

    def __str__(self):
        return self.name

class Groceryitem(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=False)
    grocerylist = models.ForeignKey(Grocerylist, on_delete=models.CASCADE)
    def __str__(self):
        return self.name