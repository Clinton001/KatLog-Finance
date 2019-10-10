from django.db import models
from django.utils import timezone

# Create your models here.

class KatLog_Finance(models.Model):
	title	=	models.CharField(max_length=100, default=True) #Blog title
	Author 	=	models.CharField(max_length=20) #Blog Author name
	Body	=	models.TextField()#Blog Full context.
	Sub_Bdy = 	models.CharField(max_length=300, default=True)#Blog Subtitle
	Sub_title =	models.CharField(max_length=70, default=True)	#Blog Subtitle
	image	=	models.ImageField( upload_to="MediaLib") #Blog uploaded images
	Date_posted	=	models.DateTimeField(default=timezone.now) #Time which the blog was posted.
	
	Source	=	models.CharField(max_length=20) #Blog source if any.



	