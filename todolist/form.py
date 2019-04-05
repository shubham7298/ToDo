from django import forms 
from .models import TodoList

class todoForm(forms.ModelForm):
	
	class Meta:
		model = TodoList
		fields = ('title', 'content', 'category', 'due_date')
