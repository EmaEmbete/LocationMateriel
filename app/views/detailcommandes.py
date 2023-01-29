from django.http import HttpRequest
from django.shortcuts import redirect,render
from app.models import Detailcommande, Commande, Client, Responsable, Typeoper
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from app.forms import DetailcommandeForm



def index(request):
      # permission
   
    assert isinstance(request,HttpRequest)
    
    detailcommande = Detailcommande.objects.all()
    return render(
        request,
        'app/detailcommandes/index.html',
        {
            'detailcommandes':detailcommande,
            
            
        }
    )
    
    
        
def create(request):
    commande = Commande.objects.latest('CodeCommande')
    materiel = Materiel.objects.all()
    responsable = Responsable.objects.all()
    typeoper = Typeoper.objects.filter(id =1)
    form = DetailcommandeForm()
    return render(
        request,
        'app/detailcommandes/create.html',
        {
            'form': form,
            'commandes': commande,
            'materiels': materiel,
            'typeopers': typeoper,
            'responsable' : responsable,

        }
    )
    
    
def store(request):
    if request.method == 'POST' :
        form = DetailcommandeForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, la commande est enregistrée avec succès")
        return redirect('/detailcommandes/create')
    
    

def edit(request, id):
    assert isinstance(request,HttpRequest)
    if request.method == "GET" :
        if id == 0:
            form = DetailcommandeForm()
        else:
            detailcommande = Detailcommande.objects.get(pk=id)
            form = DetailcommandeForm(instance=detailcommande)
        return render(
            request,
            'app/detailcommandes/edit.html',
            {
                'form': form
            }
        )
        # update
    else:
        if id == 0:
            form = DetailcommandetForm(request.POST)
        else:
            detailcommande = Detailcommande.objects.get(pk=id)
            form=DetailcommandeForm(request.POST,instance=detailcommande)
        if form.is_valid():
            
            form.save()
            messages.success(request,"Modification des infor du a reussi !!")
        return redirect('/detailcommandes') 
    
def delete(request, id):
    detailcommande = Detailcommande.objects.get(pk=id)
    detailcommande.delete()
    return redirect('/detailcommandes')         