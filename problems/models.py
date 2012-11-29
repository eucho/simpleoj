from django.db import models

# Create your models here.
class Problem(models.Model):
	def __unicode__(self):
		return self.title
	title = models.CharField(max_length=50)
	description = models.CharField(max_length=10000)
	time_limit = models.IntegerField()

class Submission(models.Model):
	def __unicode__(self):
		return str(self.problem_id) + ' ' + self.result
	problem_id = models.ForeignKey(Problem)
	submit_time = models.DateTimeField()
	source = models.CharField(max_length=10000)
	result = models.CharField(max_length=10)
