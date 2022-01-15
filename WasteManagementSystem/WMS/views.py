from django.shortcuts import render
from django.http import HttpResponse
def home(request):
    return render(request, 'home.html',)
def about(request):
    return render(request,'about.html')
def Complaint(request):
    return render(request,'complaint.html')
# Create your views here.
