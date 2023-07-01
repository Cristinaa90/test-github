from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	published_date = models.DateTimeField(blank=True, null=True)

	def __str__(self):
		return f'{self.title}-{self.created_date}'



