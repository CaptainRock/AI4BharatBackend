from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.TextField()
    language = models.TextField()

class Sentence(models.Model):
	project = models.ForeignKey(Project, on_delete=models.CASCADE)
	original_sentence = models.TextField()
	translated_sentence = models.TextField()


