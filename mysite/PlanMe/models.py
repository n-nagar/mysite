from django.db import models

# Create your models here.

class User(models.Model):
	gid = models.CharField(max_length=64)
	name = models.CharField(max_length=64)
	image_url = models.CharField(max_length=1024,null=True)
	email = models.CharField(max_length=256,null=True)
	user_tok = models.CharField(max_length=1024)
	last_session = models.CharField(max_length=1024, null=True)

