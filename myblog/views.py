from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView 
from .models import Post 

# Create your views here.

#def homepage(request):
#    return render(request,'homepage.html', {})

class HomePageView(ListView):
    model = Post
    template_name = 'homepage.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'

class AddPostView(CreateView):
    model = Post
    template_name = 'addpost.html'
    fields = '__all__'