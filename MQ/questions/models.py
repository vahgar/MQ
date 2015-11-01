from django.db import models
from account.models import CustomUser
# Create your models here.

class Topic(models.Model):
	name = models.CharField(max_length=40)
	url = models.URLField(max_length = 100, default = '',null=True,blank=True)

	def __str__(self):
		return self.name

class Question(models.Model):
    title = models.CharField(max_length = 256)
    desc = models.CharField(max_length = 1024, default = '')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    by = models.ForeignKey(CustomUser)
    topics = models.ManyToManyField(Topic)

    def __str__(self):
    	return self.title

class Answer(models.Model):
    question = models.ForeignKey(Question, related_name = 'answers')
    text = models.CharField(max_length = 1024)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    by = models.ForeignKey(CustomUser)
    is_spam = models.BooleanField(default = False)
    upvoted_by = models.ManyToManyField(CustomUser, related_name = 'answers_upvoted', blank = True)
    downvoted_by = models.ManyToManyField(CustomUser, related_name = 'answers_downvoted', blank = True)

    def __str__(self):
    	return self.question