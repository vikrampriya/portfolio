from django.db import models
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Blog Post
class Post(models.Model):
	title 				= models.CharField(max_length=400, default="No Title Set")
	date  				= models.DateTimeField('Date Published')
	image				= models.CharField(max_length=400, default="./ProjectPostPlaceHolder.png")
	content 			= models.TextField()
	is_project 			= models.BooleanField(default=False)
	short_description 	= models.TextField(default="A Blog Post")
	slug				= models.SlugField(unique=True, max_length=200)
	published 			= models.BooleanField(default=False)

	# Used for debugging
	def __str__(self):
		return self.title + ": " + self.short_description

	# Used to get perma-link to specific blog post
	def get_absolute_url(self):
		return reverse('blog.views.post', args=[self.slug])

