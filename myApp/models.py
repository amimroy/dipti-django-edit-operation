from django.db import models

# Create your models here.
class studentModel(models.Model):
    Name=models.CharField(max_length=20)
    Roll=models.CharField(max_length=20)
    City=models.CharField(max_length=20)

    def __str__(self):
        return self.Name+''+self.Roll