# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class TodoList(models.Model): 
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=250) # a varchar
	content = models.CharField(max_length=1000,blank=True) # a text field 
	category = models.IntegerField(choices=(
    (1, ("Not Started")),(2, ("In Progress")),(3, ("Done"))
), default=1)
	created = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date
	due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d")) # a date

	class Meta:
		# print(" -->> ",User.get_username())
		ordering = ["-created"] #ordering by the created field

	def __str__(self):
		return self.title #name to be shown when called
