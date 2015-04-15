from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):

	# How the information is displayed when creating a new post
	fieldsets = [
		('Meta', 		{'fields' : ['title', 'date', 'short_description', 'is_project', 'slug', 'published']}),
		('Content',		{'fields' : ['content', 'image']}),	
	]

	# How the information is displayed when viewing all posts. 
	list_display = ('title','short_description', 'is_project' )
	# fields to filter the change list with
	list_filter = ['date']
	# fields to search in change list
	search_fields = ['title', 'short_description', 'content']
	# enable the date drill down on change list
	date_hierarchy = 'date'
	# enable the save buttons on top on change form
	save_on_top = True
	# prepopulate the slug from the title - big timesaver!
	prepopulated_fields = {"slug": ("title",)}





admin.site.register(Post, PostAdmin)