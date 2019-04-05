# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import TodoList
import datetime
from .form import todoForm

def index(request):
	todos = TodoList.objects.all() 
	if request.method == 'POST':
		print("post toh hai",request.user.id)
		form = todoForm(request.POST)
		if form.is_valid():
			print("valid bhi hai")
			instance=form.save(commit=False)
			instance.owner=request.user
			instance.save()
			# form.save()
			return redirect("/todo")
		else:
			print("--------------------------------")
			print(form.errors)


	form = todoForm()
	return render(request, 'form.html', {'form':form})

