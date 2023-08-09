from django.db import models
from django.urls import reverse
# Create your models here.

class School(models.Model):
    ScName=models.CharField(max_length=50)
    ScPrincipal=models.CharField(max_length=50)
    ScLocation=models.CharField(max_length=50)
    def __str__(self):
        return self.ScName
    
    def get_absolute_url(self):
        return reverse('School_detail',kwargs={"pk":self.pk})
    
class Student(models.Model):
    Sname=models.CharField(max_length=50)
    Sage=models.IntegerField()
    ScName=models.ForeignKey(School,on_delete=models.CASCADE,related_name='nvn')
    
    def __str__(self):
        return self.Sname
    
    


