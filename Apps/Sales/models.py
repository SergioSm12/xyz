from django.db import models


# Create your models here.

class ProductType(models.Model):
    id_product_type = models.AutoField(primary_key=True)
    product_type_name = models.CharField(max_length=45)

    class Meta:
        db_table = 'product_type'

    def __str__(self):
        return self.product_type_name

class Product(models.Model):
    id_product = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=45)
    fk_id_product_type = models.ForeignKey(ProductType, db_column='fk_id_product_type', on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'

    def __str__(self):
        return self.product_name

class Person(models.Model):
    id_person = models.AutoField(primary_key=True)
    person_name = models.CharField(max_length=45, blank=True, null=True)
    person_last_name = models.CharField(max_length=45)
    person_address = models.CharField(max_length=45, blank=True, null=True)
    person_phone = models.CharField(max_length=45, blank=True, null=True)
    person_dni = models.CharField(max_length=10)

    class Meta:
        db_table = 'person'
    def __str__(self):
        return self.person_name

class Provider(models.Model):
    id_provider = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    address = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=45)
    url = models.CharField(max_length=45, blank=True, null=True)
    nit = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'provider'

    def __str__(self):

       return self.name

class ProductProvider(models.Model):
    id_product_provider = models.AutoField(primary_key=True)
    stock = models.IntegerField()
    bar_code = models.CharField(max_length=45)
    fk_id_product = models.ForeignKey(Product,db_column='fk_id_product',on_delete=models.CASCADE)
    fk_id_provider = models.ForeignKey(Provider, db_column='fk_id_provider', on_delete=models.SET_NULL, null=True)

    class Meta:
        db_table = 'product_provider'

    def __str__(self):
        return str(self.fk_id_product)




class PriceProduct(models.Model):
    id_price_product = models.AutoField(primary_key=True)
    sale_price = models.DecimalField(max_digits=13, decimal_places=2)
    shop_price = models.DecimalField(max_digits=13, decimal_places=2)
    start_date = models.DateField()
    user_update = models.CharField(max_length=40)
    date_update = models.DateField()
    fk_id_product_provider = models.ForeignKey(ProductProvider, db_column='fk_id_product_provider',on_delete=models.CASCADE)

    class Meta:
        db_table = 'price_product'

    def __str__(self):
        return str(self.fk_id_product_provider)




class Tax(models.Model):
    id_tax = models.AutoField(primary_key=True)
    tax_value = models.DecimalField(max_digits=5, decimal_places=2)
    tax_name = models.CharField(max_length=70)
    creation_date = models.DateField()

    class Meta:
        db_table = 'tax'

    def __str__(self):
        return self.tax_name

class TaxPriceProduct(models.Model):
    id_tax_price_product = models.AutoField(primary_key=True)
    fk_id_price_product = models.ForeignKey(PriceProduct, db_column='fk_id_price_product', on_delete=models.CASCADE)
    fk_id_tax = models.ForeignKey(Tax, db_column='fk_id_tax', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tax_price_product'

    def __str__(self):
        return str(self.fk_id_price_product)



class Ticket(models.Model):
    id_ticket = models.AutoField(primary_key=True)
    ticket_date = models.DateField()
    half_payment = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    fk_id_person_cashier = models.ForeignKey(Person, related_name='fk_id_person_cashier', on_delete=models.CASCADE, null=True)
    fk_id_person_customer = models.ForeignKey(Person, related_name='fk_id_person_customer', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'ticket'

    def __str__(self):
        return str(self.fk_id_person_customer)



class PersonType(models.Model):
    id_person_type = models.AutoField(primary_key=True)
    person_type_name = models.CharField(max_length=45)

    class Meta:
        db_table = 'person_type'

    def __str__(self):
        return self.person_type_name

class TicketDetail(models.Model):
    id_ticket_detail = models.AutoField(primary_key=True)
    amount = models.IntegerField()
    devolution_request = models.DateField(blank=True, null=True)
    devolution_approved = models.DateField(blank=True, null=True)
    description_devolution = models.CharField(max_length=70, blank=True, null=True)
    fk_id_tax_price_product = models.ForeignKey(TaxPriceProduct, db_column='fk_id_tax_price_product',on_delete=models.CASCADE)
    fk_id_ticket = models.ForeignKey(Ticket, db_column='fk_id_ticket', on_delete=models.CASCADE)
    fk_id_person_administrator = models.ForeignKey(Person, db_column='fk_id_person_administrator',on_delete=models.SET_NULL, blank=True, null=True)

    class Meta:
        db_table = 'ticket_detail'

    def __str__(self):
        return str(self.fk_id_tax_price_product)
class PersonPersonType(models.Model):
    id_person_person_type = models.AutoField(primary_key=True)
    fk_id_person_type = models.ForeignKey(PersonType, db_column='fk_id_person_type', on_delete=models.CASCADE)
    fk_id_person = models.ForeignKey(Person, db_column='fk_id_person', on_delete=models.CASCADE, related_name='persons')

    class Meta:
        db_table = 'person_person_type'

