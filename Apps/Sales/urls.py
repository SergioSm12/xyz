from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='home'),
    path('createProduct/', views.createProduct,name='createProduct'),
    path('deleteProduct/<id_product>', views.deleteProduct,name='deleteProduct'),
    path('editProduct/<id_product>/', views.editProduct, name='editProduct'),
    path('listTypeProduct/', views.listTypeProduct, name='listTypeProduct'),
    path('createProductType/', views.createProductType, name='createProductType'),
    path('editProductType/<id_product_type>/', views.editProductType, name='editProductType'),
    path('deleteProductType/<id_product_type>', views.deleteProductType, name='deleteProductType'),
    path('listProvider/', views.listProvider, name='listProvider'),
    path('providerData/<id_provider>', views.providerData, name='providerData'),
    path('list2Provider/', views.list2Provider, name='list2Provider'),
    path('createProvider/', views.createProvider, name='createProvider'),
    path('deleteProvider/<id_provider>', views.deleteProvider, name='deleteProvider'),
    path('createProductProvider/',views.createProductProvider, name='createProductProvider'),
    path('listPriceProduct/', views.listPriceProduct, name='listPriceProduct'),
    path('listTicket/<person_dni>', views.listTicket, name='listTicket'),
    path('listCustomers/', views.listCustomers, name='listCustomers'),
    path('list2PriceProduct/', views.list2PriceProduct, name='list2PriceProduct'),
    path('createPriceProduct/', views.createPriceProduct, name='createPriceProduct'),
    path('editPriceProduct/<id_price_product>', views.editPriceProduct, name='editPriceProduct'),
    path('deletePriceProduct/<id_price_product>', views.deletePriceProduct, name='deletePriceProduct'),
    path('listTaxPriceProduct/', views.listTaxPriceProduct, name='listTaxPriceProduct'),
    path('assignTax/', views.assignTax, name='assignTax'),
    path('listPerson/', views.listPerson, name='listPerson'),
    path('assingPersonType/', views.AssingPersonType, name='assingPersonType'),
    path('createPerson/', views.createPerson, name='createPerson'),
    path('editPerson/<id_person>', views.editPerson, name='editPerson'),
    path('deletePerson/<id_person>', views.deletePerson, name='deletePerson'),
    path('listTicketDetail/', views.listTicketDetail, name='listTicketDetail'),
    path('createTicketDetail/', views.createTicketDetail, name='createTicketDetail'),
    path('editTicketDetail/<id_ticket_detail>', views.editTicketDetail, name='editTicketDetail'),
    path('deleteTicketDetail/<id_ticket_detail>', views.deleteTicketDetail, name='deleteTicketDetail'),




]