from django.db import models

# Create your models here.
class Student(models.Model):

     std_id   = models.AutoField(primary_key = True)  #msg id
     name     = models.CharField(max_length=50)  # contact's name
     roll     = models.CharField(max_length=50)  # contact's name
     age      = models.CharField(max_length=50)	# contact's email
     phone    = models.CharField(max_length=13)  # contact's phone

     address    = models.TextField(max_length=1200)	# contact's reqiurement subject


     def __str__(self):

        return str(self.std_id) + " \ "  + self.name + " \ " + self.roll  + " \ " +self.age
