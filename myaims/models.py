from django.db import models
from django.utils import timezone


class Aim(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_date = models.DateTimeField(
    	default=timezone.now())
    start_date = models.DateTimeField(
    	blank=True, null=True)
    deadline = models.DateTimeField(
    	blank=True, null=True)

    def start(self):
        self.start_date = timezone.now()
        self.save()

    def achieve(self):
    	self.deadline = timezone.now()
    	self.save()

    def __str__(self):
        return self.title

class Task(models.Model):
	TASK_STATES = (
		('cr','created'),
		('in','in progress'),
		('done','done'),
	)
	to_aim = models.ForeignKey(Aim, on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	description = models.TextField()
	state = models.CharField(max_length=20, choices=TASK_STATES)
	start_date = models.DateTimeField(
		blank=True, null=True)

	def startTask(self):
		self.start_date = timezone.now()
		self.save()
	
	def __str__(self):
		return self.title