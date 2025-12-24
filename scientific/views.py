from django.shortcuts import render

# Create your views here.
from .models import Post

def sci_posts(request):
    posts = Post.objects.all()
    return render(request, 'scientific/scientific.html', {'posts': posts})