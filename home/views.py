from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def home(request):
    #return HttpResponse("This is my Homepage (/)")
    return render (request, 'home.html')

def about(request):
   # return HttpResponse("This is my About (/about)")
    return render (request, 'about.html')

def projects(request):
    #return HttpResponse("This is my Project (/project)")
    return render (request, 'projects.html')

def contact(request):
    if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        subject = request.POST['subject']
        desc = request.POST['desc']
        #print(name, email, phone, subject, desc)
        contact = Contact(name=name, email=email, subject=subject, phone=phone, desc=desc)
        contact.save()
        print("Contact details has been saved successfully to the db.")
   # return HttpResponse("This is my Contact (/contact)")            
    return render (request, 'contact.html')
def blog(request):
    return render(request, 'Blog.html')    
 