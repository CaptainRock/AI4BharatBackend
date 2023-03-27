from . import views

from django.urls import path

urlpatterns = [

	path('', views.homeView, name='home'),
	path('summary', views.summaryView, name ='summary'),
	path('dashboard', views.dashboardView, name = 'dashboard'),
]