from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import CreateView,DetailView
from .models import Request
def home(request):
    return render(request, 'home.html',)
def about(request):
    return render(request,'about.html')
def Complaint(request):
    return render(request,'complaint.html')
#def Login(request):
    return render(request, 'login.html')
    model=User
def Signup(request):
    return render(request, 'signup.html')
def Services(request):
    return render(request,'services.html')  
def Contact(request):
    return render(request,'contact.html')  
def MechanicalSweeping(request):
    return render(request,'mechanicaSweeping.html')
def WasteCollection(request):
    return render(request,'WasteCollection.html')
def MechanicalWashing(request):
    return render(request,'MechanicalWashing.html')


# Create your views here.
class RequestCreateView(CreateView):
    model=Request
    template_name="complaint.html"
    fields=['name','email','phone','address','zone','complaint','image','date_posted']
class RequestDetailView(DetailView):
    model=Request
    template_name='request_detail.html'