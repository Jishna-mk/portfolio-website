from django.shortcuts import render,redirect

# Create your views here.
def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")    

def contact(request):
    return render(request,"contact.html")
    
def skills(request):
    return render(request,"skills.html")
