from django.db import models
from django.conf import settings



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
       
    class Meta:
        abstract=True



class Region(BaseModel):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class District(BaseModel):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='districts')
    
    def __str__(self):
        return self.name