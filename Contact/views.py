from django.shortcuts import render 

def Contact_view(request): 
    return render(request, "contact_view.html") 