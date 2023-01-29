from django.http import HttpRequest
from django.shortcuts import redirect,render
from app.models import Commande, Client
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from app.forms import CommandeForm
from django.db.models import Max



def index(request):
      # permission
   
    assert isinstance(request,HttpRequest)
    
    commandes = Commande.objects.all()
    return render(
        request,
        'app/commandes/index.html',
        {
            'commandes':commandes,
            
            
        }
    )
    
    
        
def create(request):
    assert isinstance(request, HttpRequest)
    cmdes = Commande.objects.all()
    if cmdes.count() == 0 :
        code = 101
    else :
        code = cmdes.aggregate(max=Max('CodeCommande'))['max'] + 1
    client = Client.objects.latest('id')
    # client = Client.objects.latest('NomClient')
    form =CommandeForm()
    return render(
        request,
        'app/detailcommandes/create.html',
        {
            'form': form,
            'codes':code,
            'clients':client,
        }
    )
    
    
def store(request): 
    cmdes = Commande.objects.all()
    if cmdes.count() == 0 :
        code = 101 
    else :
        code = cmdes.aggregate(max=Max('CodeCommande'))['max'] + 1
    if request.method == 'POST':
        client = request.POST['client']
        DateCommande = request.POST['DateCommande']
        data = Commande.objects.create(client_id = client, CodeCommande = code, DateCommande = DateCommande)

        data.save()
        messages.success(request,"La commande a été Enregistré")
        return redirect('/detailcommandes/create')
    
    

def edit(request, id):
    assert isinstance(request,HttpRequest)
    if request.method == "GET" :
        if id == 0:
            form = CommandeForm()
        else:
            commande = Commande.objects.get(pk=id)
            form = CommandeForm(instance=commande)
        return render(
            request,
            'app/commandes/edit.html',
            {
                'form': form
            }
        )
        # update
    else:
        if id == 0:
            form = CommandeForm(request.POST)
        else:
            commande = Commande.objects.get(pk=id)
            form = CommandeForm(request.POST,instance=commande)
        if form.is_valid():
            form.save()
            messages.success(request,"Modification des infor a reussi !!")
        return redirect('/commandes') 



    
def delete(request, id):
    commande = Commande.objects.get(pk=id)
    commande.delete()
    return redirect('/commandes')         