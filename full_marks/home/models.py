from django.db import models

# Create your models here.
class notesCategory (models.Model):
    name=models.CharField(max_length=200)
    def __str__ (self):
        return self.name
class notesContent(models.Model):
    name=models.CharField(max_length=500)
    content=models.TextField()
    date=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(notesCategory,on_delete=models.CASCADE)
    def __str__(self):
        return self.name + " " + self.category.name