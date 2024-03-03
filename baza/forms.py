from django import forms
from .models import Clientadd, CerviseClient,Mahsulottopshirish, Ishchilar

class ClientsForm(forms.ModelForm):

    class Meta:
        model = Clientadd
        fields = '__all__'
        widgets ={
            'client_name': forms.TextInput(attrs={'class': 'form-control'}),
            'client_phonenumber': forms.TextInput(attrs={'class': 'form-control'}),
            'ovner': forms.Select(attrs={'class': 'form-control'}),
            'client_reception_time': forms.TextInput()
        }

class CerviseClientForm(forms.ModelForm):
    class Meta:
        model = CerviseClient
        fields = '__all__'
        widgets = {
            'client_name': forms.Select(attrs={'class': 'form-control select2'}),
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'product_value': forms.NumberInput(attrs={'class': 'form-control'}),
            'product_color': forms.TextInput(attrs={'class': 'form-control'}),
            'service_catetegory': forms.Select(attrs={'class': 'form-control select2'}),
            'product_defective': forms.TextInput(attrs={'class':'form-control'}),
            'product_repaired' : forms.TextInput(attrs={'class':'form-control'}),
            'produtct_not_repaired': forms.TextInput(attrs={'class':'form-control'}),
            'clien_service_price' : forms.NumberInput(attrs={'class':'form-control'}),
            'product_repairman' :   forms.Select(attrs={'class':'form-control select2'}),
        }

class Cerviceend(forms.ModelForm):
    class Meta:
        model = Mahsulottopshirish
        fields = '__all__'

class AddWorkerForm(forms.ModelForm):
    
    class Meta:
        model = Ishchilar
        fields = '__all__'
        widgets = {
            'worker_name': forms.TextInput(attrs={'class': 'form-control'}),
            'worker_surname': forms.TextInput(attrs={'class': 'form-control'}),
            'worker_age' : forms.NumberInput(attrs={'class':'form-control'}),
            'worker_stage' :forms.NumberInput(attrs={'class':'form-control'}),
        }
