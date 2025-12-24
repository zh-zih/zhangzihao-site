from django.shortcuts import render

# Create your views here.
from .models import Post

def aes_posts(request):
    posts = Post.objects.all()
    return render(request, 'aesthetic/aesthetic.html', {'posts': posts})