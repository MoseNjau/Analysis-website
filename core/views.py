from django.shortcuts import render,redirect
from .models import Contact
from django.contrib import messages

def index(request):
    return render(request, "core/index.html")

def about(request):
    return render(request, "core/about.html")

def contact(request):
    if request.method=="POST":
        name = request.POST.get("name")
        email =request.POST.get("email")
        subject =request.POST.get("subject")
        message =request.POST.get("meessage")

        contact.objects.create(full_name=name, email=email ,subject=subject ,message=message)
        messages.success(request, "Your message has been set successfully")
        return redirect("index")
    return render(request, "core/contact.html")

def pricing(request):
    return render(request, "core/pricing.html")

def trainers(request):
    return render(request, "core/trainers.html")

def courses(request):
    return render(request,"core/courses.html")

def events(request):
    return render(request, "core/events.html")

