from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Task(models.Model):
	"""docstring for Task"""
	context = models.CharField(max_length=500)
	pub_date = models.DateTimeField('date published')
	status = models.IntegerField(default=0)
	deadline =  models.DateTimeField('date published')