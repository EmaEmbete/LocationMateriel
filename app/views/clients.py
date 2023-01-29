from django.http import HttpRequest
from django.shortcuts import redirect,render
from app.models import Client
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from app.forms import ClientForm



def index(request):
      # permission
   
    assert isinstance(request,HttpRequest)
    
    clients = Client.objects.all()
    return render(
        request,
        'app/clients/index.html',
        {
            'clients':clients,
            
            
        }
    )
    
    
        
def create(request):
    form =ClientForm()
    return render(
        request,
        'app/clients/create.html',
        {
            'form': form
            }
        )
    
    
def store(request):
    if request.method == 'POST' :
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Le client a été Enregistré")
        return redirect('/commandes/create')
    
    

def edit(request, id):
    assert isinstance(request,HttpRequest)
    if request.method == "GET" :
        if id == 0:
            form = ClientForm()
        else:
            client = Client.objects.get(pk=id)
            form = ClientForm(instance=client)
        return render(
            request,
            'app/clients/edit.html',
            {
                'form': form
            }
        )
        # update
    else:
        if id == 0:
            form = ClientForm(request.POST)
        else:
            client = Client.objects.get(pk=id)
            form = ClientForm(request.POST,instance=client)
        if form.is_valid():
            
            form.save()
            messages.success(request,"Modification des infor du a reussi !!")
        return redirect('/clients') 
    
def delete(request, id):
    elev = Client.objects.get(pk=id)
    client.delete()
    return redirect('/clients')         