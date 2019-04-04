from django.contrib.auth import views as auth_views
from django.urls import path
from .views import home, register

urlpatterns = [
	path('login/',auth_views.LoginView.as_view(), name='login'),
	# path('logout/', auth_views.LogoutView.as_view(template_name = 'registration/logged_out.html'), name='logout'),
	path('logout/', auth_views.LogoutView.as_view(), {'template_name': 'registration/logged_out.html'}, name='logout'),
	path('',home),
	path('register/',register, name='register')
]