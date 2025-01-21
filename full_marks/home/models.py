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
class examSubject(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name
class subjectCategory(models.Model):
    name=models.CharField(max_length=200)
    text=models.TextField()
    subject=models.ForeignKey(examSubject,on_delete=models.CASCADE)
    def __str__(self):
        return self.name + "-" + self.subject.name
class question(models.Model):
    title=models.CharField(max_length=1000)
    correctAnswer=models.CharField(max_length=1000)
    otherAnswers=models.CharField(max_length=5000)
    category=models.ForeignKey(subjectCategory,on_delete=models.CASCADE)
    def __str__(self):
        return self.title + " - " + self.category