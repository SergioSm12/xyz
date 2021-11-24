from django import forms
from .models import Product, ProductType, Provider, ProductProvider, PriceProduct,TaxPriceProduct, PersonPersonType, Person, TicketDetail

class ProductForm(forms.ModelForm):
    class Meta:
        model= Product
        fields= '__all__'

class ProductTypeForm(forms.ModelForm):
    class Meta:
        model= ProductType
        fields= '__all__'


class ProviderForm(forms.ModelForm):
    class Meta:
        model = Provider
        fields = '__all__'

class ProductProviderForm(forms.ModelForm):
    class Meta:
        model = ProductProvider
        fields = '__all__'

class PriceProductForm(forms.ModelForm):
    class Meta:
        model = PriceProduct
        fields = '__all__'

        widgets ={
            "start_date": forms.SelectDateWidget(),
            "date_update": forms.SelectDateWidget()
        }

class TaxPriceProductForm(forms.ModelForm):

    class Meta:
        model= TaxPriceProduct
        fields= '__all__'

class PersonTypeForm(forms.ModelForm):
    class Meta:
        model= PersonPersonType
        fields= '__all__'

class PersonForm(forms.ModelForm):
    class Meta:
      model=Person
      fields='__all__'

class TicketDetailForm(forms.ModelForm):
    class Meta:
        model= TicketDetail
        fields=('amount', 'fk_id_tax_price_product', 'fk_id_ticket')
        labels = {
            'fk_id_tax_price_product': 'Product',
            'fk_id_ticket': 'Ticket Customer',
        }
        widgets = {
            "amount": forms.TextInput(attrs={'class':'form-control'}),
            "fk_id_tax_price_product": forms.Select(attrs={'class':'form-control'}),
            'fk_id_ticket': forms.Select(attrs={'class':'form-control'}),
        }
