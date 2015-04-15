from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post
from django.shortcuts import get_object_or_404
import random

def index(request):
	# Get the blog posts that are published. 
	posts = Post.objects.filter(published=True)
	# Return the rendered template. 
	return render(request, 'blog/index.html', {'posts': posts})

def aboutme(request):
	# Return the rendered template. 
	return render(request, 'blog/aboutme.html')

def post(request, slug):
	# Get the actual Post object 
	post = get_object_or_404(Post, slug=slug)

	# Get some other stories 
	posts = Post.objects.filter(published=True)
	posts = [p for p in posts if p.title != post.title]
	posts = posts[0:3]
	random.shuffle(posts)

	# Return the Post object 
	return render(request, 'blog/post.html', {'post': post, 'posts': posts})

def contact(request):
	return render(request, 'blog/contact.html')