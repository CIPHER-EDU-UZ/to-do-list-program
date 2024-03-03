from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import *
from .forms import ClientsForm, CerviseClientForm,Cerviceend,AddWorkerForm
#add home page
def home(request):
    return render(request, 'index.html')

#add function show_clients
def clients(request):
    return render(request, 'pages/clients.html')

#def add function add-client
def clientregister(request):
    context = {}
    if request.method == 'GET':
        context['form']= ClientsForm()
        return render(request, 'pages/addclients.html', context=context)
    else:
        forms = ClientsForm(request.POST)
        if forms.is_valid():
            forms.save()
            context['form']= ClientsForm()
            return render(request, 'pages/addclients.html', context=context)
#add service

def service(request):
    context = {}
    if request.method == 'GET':
        context['form']= CerviseClientForm()
        return render(request, 'pages/clientservice.html', context=context)
    else:
        forms = CerviseClientForm(request.POST)
        if forms.is_valid():
            forms.save()
            context['form']= CerviseClientForm()
            return render(request, 'pages/clientservice.html', context=context)
        
def clientend(request):
    context = {}
    if request.method == 'GET':
        context ['form'] = Cerviceend()
        return HttpResponse(f"hatolik")
    else:
        forms = Cerviceend(request.POST)
        if forms.is_valid():
            context['form'] = Cerviceend()
            return render(request, 'pages/clientend.html', context=context)
#def add items page
def items(request):
    return render(request, 'pages/items.html')
#add items_add
def qushish(request):
    return render(request, 'pages/additems.html')
#add organizations
def addorganizations(request):
    return render(request, 'pages/addorganizations.html')
#add organizations
def organizations(request):
    return render(request,'pages/organizations.html')

#add qarzdorliklar 
def qarz(request):
    return render(request, 'pages/qarz.html')

#add invoiceses
def invoice(request):
    return render(request, 'pages/invoice.html')

#add worker_add 
def addworker(request):
    context = {}
    if request.method == 'GET':
        context['form']= AddWorkerForm()
        return render(request, 'pages/addworker.html', context=context)
    else:
        forms = AddWorkerForm(request.POST)
        if forms.is_valid():
            forms.save()
            context['form']= AddWorkerForm()
            return render(request, 'pages/addworker.html', context=context)
    #return render (request, 'pages/addworker.html')

# add worker
def workers(requst):
    return render (requst, 'pages/workers.html')

