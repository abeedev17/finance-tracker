from djongo import models

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
