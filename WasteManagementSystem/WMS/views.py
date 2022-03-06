from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import CreateView, DetailView, ListView
from .models import Request, Manager


def home(request):
    return render(request, 'home.html', )


def about(request):
    return render(request, 'about.html')


def Complaint(request):
    return render(request, 'complaint.html')


def Signup(request):
    return render(request, 'signup.html')


def Services(request):
    return render(request, 'services.html')


def Contact(request):
    return render(request, 'contact.html')


def MechanicalSweeping(request):
    return render(request, 'mechanicaSweeping.html')


def WasteCollection(request):
    return render(request, 'WasteCollection.html')


def MechanicalWashing(request):
    return render(request, 'MechanicalWashing.html')


# Complaints Views

class RequestCreateView(CreateView):
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
        return Request.objects.filter(zone=manager.zone)


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
