from django.db import models

from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.urls import reverse

from django.db.models.signals import post_save
from django.dispatch import receiver


"""
UserAccount model is for storing user account entry 

Attributes:
---------------
userName: Indicates the character field for user name
userEmail: Indicates the character field  for user email
userPhone: Indicates the character field for user phone number
"""


class userAccount(models.Model):
	userName = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	fullName = models.CharField(max_length=200, null=True)
	userPhone = models.CharField(max_length=200, null=True)
	userEmail = models.CharField(max_length=200, null=True)
	dateCreated = models.DateTimeField(auto_now_add=True, null=True)


	def __str__(self):
		return str(self.userName)

class blog(models.Model):

  """
    This model is for storing blog item 
    Attributes:
    ------------
    title : Indicates the character file for title
    author : Indicates the character file for author
    Body : This will create a character field to store body 


    Method:
    -----------
    get_absolute_urle: This will return url
    
    """


    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete = models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title + ' | ' + str(self.author)
    def get_absolute_url(self):
        #return reverse('blog-detail', args=(str(self.id)))
        return reverse('blog')





class CustomUser(AbstractUser):
    user_type_data=((1,"HOD"),(3,"Student"))
    user_type=models.CharField(default=1,choices=user_type_data,max_length=10)

class AdminHOD(models.Model):
    id=models.AutoField(primary_key=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects=models.Manager()




""" 
Student model will creates an item for student field


"""

class Students(models.Model):
    id=models.AutoField(primary_key=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    fcm_token=models.TextField(default="")
    objects = models.Manager()



class NotificationStudent(models.Model):
    id = models.AutoField(primary_key=True)
    student_id = models.ForeignKey(Students, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()







