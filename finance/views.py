from django.shortcuts import render
from .models import KatLog_Finance
from django.views.generic import ListView, DetailView
# Create your views here.


	

class home_view(ListView):
	model	=	KatLog_Finance #model name

	template_name =  "finance/Home.html" #name of the template that access this data
	context_object_name = "my_obj" #name of the object
	ordering = ["-Date_posted"] # this render the post by the current post
	paginate_by = 3 #allows a number of post to be in a page



class Blog_Page(ListView):
	model = KatLog_Finance
	template_name	= "finance/Posts.html"
	context_object_name = "posts"
	ordering	=	["-Date_posted"]
	paginate_by = 2


class Blog_post(DetailView):
	model = KatLog_Finance
	template_name	= "finance/blog_post.html" #This code is responsible for reading each detailed post.


def about_page_view(request):
	return render(request, "finance/About.html", {})





def contact_page_view(request):
	return render(request, "finance/Contact.html", {})
