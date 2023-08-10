from django.db import models
from base.models import BaseModel
# Create your models here.

class ServiceType(BaseModel):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.name}'