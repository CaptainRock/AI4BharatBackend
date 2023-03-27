from django.shortcuts import render
from wikipediaapi import Wikipedia
import nltk
import django.apps
# Create your views here.
from .models import Project, Sentence

nltk.download("punkt")

def homeView(request):
	return render(request, 'ai4bharat/index.html')

def summaryView(request):


	search = request.GET.get('search')

	
	if not search:
		search="ai4bharat"

	language = request.GET.get('langs')
	intro = Wikipedia().page(search).summary

	#split summary into sentences

	sentences = nltk.sent_tokenize(intro)	
	print(intro)
	context = {
		
		'title': search,
		'summary': intro,
		'sentences': sentences

	}
	if search and search != "ai4bharat":
		project = Project(title=search, language=language)
		project.save()
		for s in sentences:
			my_sentence = Sentence(project_id = project.id, original_sentence = s)
			my_sentence.save()
		
	else:

		print(django.apps.apps.get_models())
		for name, value in request.GET.items():
        		#print(f"{name}: {value}")
			print(Sentence.objects.all().values())
			objs = Sentence.objects.filter(original_sentence__contains=name).update(translated_sentence=value)
			
			

	return render(request, 'ai4bharat/summary.html', context)

def dashboardView(request):
	
	projects = Project.objects.all().values()
	context = {
		
		'projects': projects

	}
	return render(request, 'ai4bharat/dashboard.html', context)


