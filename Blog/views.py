from django.shortcuts import render 
from .models import MyModel

def Blog_view(request): 
    mymodels = MyModel.objects.all()
    return render(request, 'blog_view.html', {'mymodels': mymodels})
