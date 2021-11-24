from django.shortcuts import render, redirect, get_object_or_404,get_list_or_404
from .models import *
from django.db.models import Sum
from django.views.generic import ListView
from .forms import *

import os
from django.conf import settings
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from xhtml2pdf import pisa



# Create your views here.
def home(request):
    data ={
        'products' : Product.objects.all(),
    }

    return render(request, 'Home.html', data)


def createProduct(request):
    data = {
        'form': ProductForm()
    }
    if request.method == 'POST':
        formulario = ProductForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Guardado Correctamente"
        else:
            data["form"] = formulario
    return render(request, 'product/createProduct.html', data)

def editProduct(request, id_product):
    products= get_object_or_404(Product, id_product=id_product)
    data = {
        'form': ProductForm(instance=products)
    }

    if request.method == 'POST':
        formulario=ProductForm(data=request.POST, instance= products,)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='/')
        data['form'] = formulario
    return  render(request,'product/editProduct.html', data )

def deleteProduct(request,id_product):
    product=Product.objects.get(id_product=id_product)
    product.delete()
    return  redirect('/')

def listTypeProduct(request):
    productTypeList=ProductType.objects.all()

    return render(request, 'TypeProduct/listTypeProduct.html', {'productTypeList': productTypeList})

def createProductType(request):
    data = {
        'form': ProductTypeForm()
    }
    if request.method == 'POST':
        formulario = ProductTypeForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listTypeProduct')
        else:
            data["form"] = formulario
    return render(request, 'TypeProduct/createProductType.html', data )

def editProductType(request, id_product_type):
    products_type= get_object_or_404(ProductType, id_product_type=id_product_type)
    data = {
        'form': ProductTypeForm(instance=products_type)
    }

    if request.method == 'POST':
        formulario=ProductTypeForm(data=request.POST, instance= products_type)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listTypeProduct')
        data['form'] = formulario
    return render(request,'TypeProduct/editProductType.html', data )

def deleteProductType(request,id_product_type):
    productType=ProductType.objects.get(id_product_type=id_product_type)
    productType.delete()
    return redirect(to='listTypeProduct')

def listProvider(request):
    provider=ProductProvider.objects.all()
    return render(request, 'Provider/listProvider.html', {'provider': provider})

def  providerData(request,id_provider):
    providers = get_object_or_404(Provider, id_provider=id_provider)
    data = {
        'form': ProviderForm(instance=providers)
    }

    if request.method == 'POST':
        formulario = ProviderForm(data=request.POST, instance=providers, )
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listProvider')
        data['form'] = formulario
    return render(request, 'Provider/providerData.html', data)

def list2Provider(request):
    provider=Provider.objects.all()
    return render(request, 'Provider/gestionProvider.html', {'provider': provider})

def createProvider(request):
    data = {
        'form': ProviderForm()
    }
    if request.method == 'POST':
        formulario = ProviderForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='list2Provider')
        else:
            data["form"] = formulario
    return render(request, 'Provider/createProvider.html', data)

def deleteProvider(request,id_provider):
    provider = Provider.objects.get(id_provider=id_provider)
    provider.delete()
    return redirect(to='list2Provider')


def createProductProvider(request):
    data = {
        'form': ProductProviderForm()
    }
    if request.method == 'POST':
        formulario = ProductProviderForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listProvider')
        else:
            data["form"] = formulario
    return render(request, 'Provider/createProductProvider.html', data)

def listPriceProduct(request):
    priceProduct=PriceProduct.objects.all()
    return render(request, 'PriceProduct/listPriceProduct.html', {'priceProduct' : priceProduct})

def listCustomers(request):
    clients=PersonPersonType.objects.all().filter(fk_id_person_type__person_type_name='Cliente')
    return render(request, 'Ticket/listCustomers.html', {'clients': clients})

def listTicket(request,person_dni):
    ticket = TicketDetail.objects.filter(fk_id_ticket__fk_id_person_customer__person_dni=person_dni)
    return render(request, 'Ticket/listTicket.html', {'ticket': ticket})

def list2PriceProduct(request):
    priceproduct=PriceProduct.objects.all()
    return render(request, 'PriceProduct/list2PriceProduct.html', {'priceproduct': priceproduct})

def createPriceProduct(request):
    data = {
        'form': PriceProductForm()
    }
    if request.method == 'POST':
        formulario = PriceProductForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='list2PriceProduct')
        else:
            data["form"] = formulario
    return render(request, 'PriceProduct/createPriceProduct.html', data)

def editPriceProduct(request,id_price_product):
    priceProduct = get_object_or_404(PriceProduct, id_price_product=id_price_product)
    data = {
        'form': PriceProductForm(instance=priceProduct)
    }

    if request.method == 'POST':
        formulario = PriceProductForm(data=request.POST, instance=priceProduct)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='list2PriceProduct')
        data['form'] = formulario
    return render(request, 'PriceProduct/editPriceProduct.html', data)

def deletePriceProduct(request,id_price_product):
    priceProduct = PriceProduct.objects.get(id_price_product=id_price_product)
    priceProduct.delete()
    return redirect(to='list2PriceProduct')

def listTaxPriceProduct(request):
    tax=Tax.objects.all()
    return render(request, 'TaxPriceProduct/listTaxPriceProduct.html', {'tax': tax})

def listPerson(request):
    listCustomer=PersonPersonType.objects.filter(fk_id_person_type__person_type_name='Cliente')
    listStaf = PersonPersonType.objects.filter(fk_id_person_type__person_type_name='Administrador') | PersonPersonType.objects.filter(fk_id_person_type__person_type_name='Cajero')
    return render(request, 'Person/listPerson.html', {'listPerson': listCustomer, 'listStaff': listStaf})

def AssingPersonType(request):
    data = {
        'form': PersonTypeForm()
    }
    if request.method == 'POST':
        formulario = PersonTypeForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listPerson')
        else:
            data["form"] = formulario
    return render(request, 'Person/assingPersonType.html', data)

def createPerson(request):
    data = {
        'form': PersonForm()
    }
    if request.method == 'POST':
        formulario = PersonForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='assingPersonType')
        else:
            data["form"] = formulario
    return render(request, 'Person/createPerson.html', data)

def editPerson(request,id_person):
    person = get_object_or_404(Person, id_person=id_person)
    data = {
        'form': PersonForm(instance=person)
    }

    if request.method == 'POST':
        formulario = PersonForm(data=request.POST, instance=person)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listPerson')
        data['form'] = formulario
    return render(request, 'Person/editPerson.html', data)

def deletePerson(request,id_person):
    person = Person.objects.get(id_person=id_person)
    person.delete()
    return redirect(to='listPerson')

def listTicketDetail(request):
        listTicketDetail= TicketDetail.objects.all()
        return render(request, 'TicketDetail/listTicketDetail.html', {'listTicketDetail': listTicketDetail})

def createTicketDetail(request):
    data = {
        'form': TicketDetailForm()
    }
    if request.method == 'POST':
        formulario = TicketDetailForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listCustomers')
        else:
            data["form"] = formulario
    return render(request, 'TicketDetail/createTicketDetail.html', data)

def editTicketDetail(request,id_ticket_detail):
    ticketdetail = get_object_or_404(TicketDetail, id_ticket_detail=id_ticket_detail)
    data = {
        'form': TicketDetailForm(instance=ticketdetail)
    }

    if request.method == 'POST':
        formulario = TicketDetailForm(data=request.POST, instance=ticketdetail)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listTicketDetail')
        data['form'] = formulario
    return render(request, 'TicketDetail/editTicketDetail.html', data)

def deleteTicketDetail(request,id_ticket_detail):
    ticketdetail = TicketDetail.objects.get(id_ticket_detail=id_ticket_detail)
    ticketdetail.delete()
    return redirect(to='listTicketDetail')

def assignTax(request):
    data = {
        'form': TaxPriceProductForm()
    }
    if request.method == 'POST':
        formulario = TaxPriceProductForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(to='listTaxPriceProduct')
        else:
            data["form"] = formulario
    return render(request, 'TaxPriceProduct/assignTax.html', data)


