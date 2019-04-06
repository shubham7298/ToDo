# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import TodoList
import datetime
from django.views import generic
from .form import todoForm

def index(request):
	todos = TodoList.objects.all() 
	print(request.get_full_path())
	if request.method == 'POST':
		print("post toh hai",request.user.id)
		form = todoForm(request.POST)
		if form.is_valid():
			print("valid bhi hai")
			instance=form.save(commit=False)
			instance.owner=request.user
			instance.save()
			# form.save()
			return redirect("/todo/0")
		else:
			print("--------------------------------")
			print(form.errors)

		if "taskDelete" in request.POST: #checking if there is a request to delete a todo
			checkedlist = request.POST["checkedbox"] #checked todos to be deleted
			for todo_id in checkedlist:
				todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
				todo.delete() #deleting todo


	form = todoForm()
	return render(request, 'form.html', {"todos": todos,'form':form})

def EditView(request, pk, *args, **kwargs):
	todos = TodoList.objects.all() 
	edit_this = TodoList.objects.get(pk=pk)
	form = todoForm( instance=edit_this)
	if request.method == 'POST':
		print("ThATS A HUGE HIT ~~~!!!")
		form = todoForm(request.POST)
		if form.is_valid():
			print("valid bhi hai")
			instance=form.save(commit=False)
			instance.owner=request.user
			instance.save()
			edit_this.delete()
			return redirect("/todo/0")
	return render(request, 'edit.html', {"todos": todos,'form':form})
