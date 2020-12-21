from django.db import models
from django.utils.translation import gettext as _
from django.utils.html import mark_safe
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .mail import sendemail

STATUS_TYPES = [
    ('pending', 'pending'),
    ('approved', 'approved'),
    ('cancelled', 'cancelled')
]

class Vitrin(models.Model):
    name = models.CharField(max_length=63)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, default=5.90)
    discount = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey(
        'VitrinCategory', on_delete=models.SET_NULL, blank=True, null=True, default=7)
    ingredient = models.CharField(max_length=511, blank=True, null=True)
    weight = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='', blank=True, null=True)
    publish = models.BooleanField(default=True)
    homepage = models.BooleanField(default=False)
    similar1 = models.ForeignKey('Vitrin', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar1_of')
    similar2 = models.ForeignKey('Vitrin', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar2_of')
    similar3 = models.ForeignKey('Vitrin', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar3_of')
    similar4 = models.ForeignKey('Vitrin', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar4_of')

    def __str__(self):
        return self.name


class VitrinCategory(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Marsipan(models.Model):
    name = models.CharField(max_length=63)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, default=12.00)
    discount = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey(
        'MarsipanCategory', on_delete=models.SET_NULL, blank=True, null=True, default=4)
    ingredient = models.CharField(max_length=511, blank=True, null=True)
    weight = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='', blank=True, null=True)
    publish = models.BooleanField(default=True)
    homepage = models.BooleanField(default=False)
    similar1 = models.ForeignKey('Marsipan', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar1_of')
    similar2 = models.ForeignKey('Marsipan', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar2_of')
    similar3 = models.ForeignKey('Marsipan', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar3_of')
    similar4 = models.ForeignKey('Marsipan', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar4_of')

    def __str__(self):
        return self.name


class MarsipanCategory(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name

class Flower(models.Model):
    name = models.CharField(max_length=63)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, default=12.00)
    discount = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey(
        'FlowerCategory', on_delete=models.SET_NULL, blank=True, null=True, default=4)
    ingredient = models.CharField(max_length=511, blank=True, null=True)
    weight = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='', blank=True, null=True)
    publish = models.BooleanField(default=True)
    homepage = models.BooleanField(default=False)
    similar1 = models.ForeignKey('Flower', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar1_of')
    similar2 = models.ForeignKey('Flower', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar2_of')
    similar3 = models.ForeignKey('Flower', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar3_of')
    similar4 = models.ForeignKey('Flower', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar4_of')

    def __str__(self):
        return self.name


class FlowerCategory(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name

class Xonca(models.Model):
    name = models.CharField(max_length=63)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, default=12.00)
    discount = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey(
        'XoncaCategory', on_delete=models.SET_NULL, blank=True, null=True, default=4)
    ingredient = models.CharField(max_length=511, blank=True, null=True)
    weight = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='', blank=True, null=True)
    publish = models.BooleanField(default=True)
    homepage = models.BooleanField(default=False)
    similar1 = models.ForeignKey('Xonca', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar1_of')
    similar2 = models.ForeignKey('Xonca', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar2_of')
    similar3 = models.ForeignKey('Xonca', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar3_of')
    similar4 = models.ForeignKey('Xonca', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar4_of')

    def __str__(self):
        return self.name


class XoncaCategory(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Cafe(models.Model):
    image = models.ImageField(upload_to='')

class Contact(models.Model):
    name = models.CharField(max_length=31)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    subject = models.CharField(max_length=31)
    message = models.TextField()

# PRODUCT_TYPE = [
#     ('Vitrin', 'Vitrin'),
#     ('Marsipan', 'Marsipan'),
#     ('Flower', 'Flower'),
#     ('Xonca', 'Xonca'),
# ]
# class ProductType(models.Model):
#     type = models.CharField(choices=PRODUCT_TYPE, max_length=8)
#     def __str__(self):
#         return self.type

class HomePageProduct(models.Model):
    vitrin = models.IntegerField(default=2)
    marsipan = models.IntegerField(default=2)
    flower = models.IntegerField(default=2)
    xonca = models.IntegerField(default=2)

class Order(models.Model):
    name = models.CharField(max_length=63)
    surname = models.CharField(max_length=63)
    email = models.EmailField(max_length=63)
    city = models.CharField(max_length=63, default="Baki")
    address = models.CharField(max_length=63)
    address2 = models.CharField(max_length=63, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    orderid = models.IntegerField(unique=True)
    sessionid = models.CharField(max_length=127, unique=True)
    # created = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(("Created at"), auto_now_add=True)
    pan = models.CharField(max_length=32, blank=True, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    status = models.CharField(choices=STATUS_TYPES, default='pending',max_length=15)
    old_status = None
    def __str__ (self):
        return self.address
    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)
        print("___")
        print("init old: ", self.old_status)
        self.old_status = self.status
        print("init old: ", self.old_status)
        print("init status: ", self.status)
    def save(self, *args, **kwargs):
        if self.old_status == None:
            self.old_status = 'pending'
        elif self.old_status != self.status:
            if self.status == 'approved' and self.old_status == 'pending':
                message = f"Yeni sifaris var http://api.purplecakeboutique.az/admin/api/order/{self.id}/change/"
                sendemail(self.email, message)
                print("________msj sent________")
                print("save status: ",self.status)
                print("save old: ", self.old_status)
        super(Order, self).save(*args, **kwargs)