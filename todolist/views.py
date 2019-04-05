# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from .models import TodoList
import datetime
from django.views import generic
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

		if "taskDelete" in request.POST: #checking if there is a request to delete a todo
			checkedlist = request.POST["checkedbox"] #checked todos to be deleted
			for todo_id in checkedlist:
				todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
				todo.delete() #deleting todo


	form = todoForm()
	return render(request, 'form.html', {"todos": todos,'form':form})

# class getUserTodo(generic.DetailView):
# 	template_name = 'todolist/form.html'
# 	model = TodoList

# 	def get_queryset(self):
# 		return TodoList.objects.all() 


