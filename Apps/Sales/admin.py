from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ('id_product_type','product_type_name')

class ProductAdmin(admin.ModelAdmin):
    list_display =('id_product','product_name', 'fk_id_product_type')

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display=('id_ticket', 'ticket_date', 'half_payment', 'fk_id_person_customer','fk_id_person_cashier')

admin.site.register(Product, ProductAdmin)