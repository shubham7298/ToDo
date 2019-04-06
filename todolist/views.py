# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import TodoList
import datetime
from django.http import HttpResponse
from django.views import generic
from .form import todoForm

def index(request):
	todos = TodoList.objects.all() 
	if request.user.id == None:
		# return HttpResponse("Please Login first to view your Todos.")
		return redirect("/")
	if request.method == 'POST':
		form = todoForm(request.POST)
		if form.is_valid():
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
	if request.user.id == None:
		return redirect("/")
		# return HttpResponse("Please Login first to edit your Todos.")
	try:
		edit_this = TodoList.objects.get(pk=pk)
	except:
		return HttpResponse("No such todo exists !")
	form = todoForm( instance=edit_this)
	if request.method == 'POST':
		form = todoForm(request.POST)
		if form.is_valid():
			instance=form.save(commit=False)
			instance.owner=request.user
			instance.save()
			edit_this.delete()
			return redirect("/todo/0")
	return render(request, 'edit.html', {"todos": todos,'form':form})
