from django.shortcuts import render, redirect
from .forms import PostForm
from .models import Blogpost

# Create your views here.

def index(request):
    return render(request, "blog.html",
                {"posts": Blogpost.objects.all()})

def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog.html")
    else:
        form = PostForm()
        return render(request, "new.html", {"form": form})