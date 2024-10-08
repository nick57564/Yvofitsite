from django.shortcuts import render 

def Blog_view(request): 
    return render(request, "blog_view.html") 