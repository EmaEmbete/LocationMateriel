from django.forms import ModelForm
from app.models import Detailcommande

class DetailcommandeForm(ModelForm):
    class Meta:
        model = Detailcommande
        fields = '__all__'