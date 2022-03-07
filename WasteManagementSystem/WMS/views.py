from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic import CreateView, DetailView, ListView
from .models import Request, Manager,Contact


def home(request):
    a_list=Request.objects.all()
    r=0
    p=0
    pend=0
    t=0
    tot=len(a_list)
    for s in a_list:
        if s.status=='PENDING':
            pend+=1
        elif s.status=='RESOLVED':
            r+=1
        elif s.status=="PROCESSING":
          p+=1
    context={
        'pending':pend,
        'resolved':r,
        'process':p,
        'total':tot,
    }
    return render(request, 'home.html',context )


def about(request):
    return render(request, 'about.html')


def Complaint(request):
    return render(request, 'complaint.html')


def Signup(request):
    return render(request, 'signup.html')


def Services(request):
    return render(request, 'services.html')




def MechanicalSweeping(request):
    return render(request, 'mechanicaSweeping.html')


def WasteCollection(request):
    return render(request, 'WasteCollection.html')


def MechanicalWashing(request):
    return render(request, 'MechanicalWashing.html')


# Complaints Views

class RequestCreateView(LoginRequiredMixin,CreateView):
    model = Request
    template_name = "complaint.html"
    fields = ['phone', 'address', 'zone', 'complaint', 'image', 'date_posted']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(RequestCreateView, self).form_valid(form)


class RequestDetailView(DetailView):
    model = Request
    template_name = 'request_detail.html'


class RequestListView(ListView):
    model = Request
    template_name = "CompList.html"

    def get_queryset(self):
        return Request.objects.filter(author=self.request.user).order_by('-date_posted')


class RequestByZoneListView(ListView):
    model = Request
    template_name = "ManagerComplaintList.html"
    ordering = ['-date_posted']

    def get_queryset(self):
        manager = Manager.objects.get(user=self.request.user)
        return Request.objects.filter(zone=manager.zone).order_by('-date_posted')


class InProgressView(View):
    def post(self, request, *args, **kwargs):
        comp_pk = kwargs.get('pk')
        comp = Request.objects.get(pk=comp_pk)
        comp.status = 'PROCESSING'
        comp.save()
        return redirect('ManagerCompList')


class ResolvedView(View):
    def post(self, request, *args, **kwargs):
        comp_pk = kwargs.get('pk')
        comp = Request.objects.get(pk=comp_pk)
        comp.status = 'RESOLVED'
        comp.save()
        return redirect('ManagerCompList')


class ContactCreateView(CreateView):
    model = Contact
    template_name = "contact.html"
    fields = ['name', 'email', 'zone', 'message', 'date_posted']
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(ContactCreateView, self).form_valid(form)

class ContactListView(ListView):
    model = Contact
    template_name = "Message.html"
    ordering = ['-date_posted']
"""
    def get_queryset(self):
        return Request.objects.filter(author=self.request.user).order_by('-date_posted')
"""
def ManagerPanel(request):
    return render (request, 'ManagerPanel.html')