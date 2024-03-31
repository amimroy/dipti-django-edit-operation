from django.db import models

# Create your models here.
class candidateModel(models.Model):
    full_name=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone_number=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    job_title=models.CharField(max_length=30)
    linkedin_profile=models.CharField(max_length=30)
    university=models.CharField(max_length=30)
    degree=models.CharField(max_length=30)
    languages=models.CharField(max_length=30)
    years_of_experience=models.CharField(max_length=30)

    def __str__(self):
        return self.full_name+'-'+self.address