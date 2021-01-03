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
    image = models.ImageField(upload_to='vitrin/', blank=True, null=True)
    publish = models.BooleanField(default=True)
    homepage = models.BooleanField(default=False)
    similar1 = models.ForeignKey('Vitrin', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar1_of')
    similar2 = models.ForeignKey('Vitrin', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar2_of')
    similar3 = models.ForeignKey('Vitrin', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar3_of')
    similar4 = models.ForeignKey('Vitrin', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar4_of')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Vitrin"
        verbose_name_plural = "Vitrin"


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
    image = models.ImageField(upload_to='marsipan/', blank=True, null=True)
    publish = models.BooleanField(default=True)
    homepage = models.BooleanField(default=False)
    similar1 = models.ForeignKey('Marsipan', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar1_of')
    similar2 = models.ForeignKey('Marsipan', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar2_of')
    similar3 = models.ForeignKey('Marsipan', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar3_of')
    similar4 = models.ForeignKey('Marsipan', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar4_of')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Marsipan"
        verbose_name_plural = "Marsipan"


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
    image = models.ImageField(upload_to='flower/', blank=True, null=True)
    publish = models.BooleanField(default=True)
    homepage = models.BooleanField(default=False)
    similar1 = models.ForeignKey('Flower', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar1_of')
    similar2 = models.ForeignKey('Flower', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar2_of')
    similar3 = models.ForeignKey('Flower', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar3_of')
    similar4 = models.ForeignKey('Flower', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar4_of')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Flower"
        verbose_name_plural = "Flower"


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
    image = models.ImageField(upload_to='xonca/', blank=True, null=True)
    publish = models.BooleanField(default=True)
    homepage = models.BooleanField(default=False)
    similar1 = models.ForeignKey('Xonca', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar1_of')
    similar2 = models.ForeignKey('Xonca', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar2_of')
    similar3 = models.ForeignKey('Xonca', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar3_of')
    similar4 = models.ForeignKey('Xonca', on_delete=models.SET_NULL, blank=True, null=True, related_name='similar4_of')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Xonca"
        verbose_name_plural = "Xonca"


class XoncaCategory(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Cafe(models.Model):
    image = models.ImageField(upload_to='cafe/')
    class Meta:
        verbose_name = "Kafe"
        verbose_name_plural = "Kafe"

class Contact(models.Model):
    name = models.CharField(max_length=31)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    subject = models.CharField(max_length=31)
    message = models.TextField()
    def __str__(self):
        return self.name + " :  " + self.subject
    class Meta:
        verbose_name = "Mektub"
        verbose_name_plural = "Mektub"


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
    created_at = models.DateTimeField(("Created at"), auto_now_add=True)
    pan = models.CharField(max_length=32, blank=True, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    status = models.CharField(choices=STATUS_TYPES, default='pending',max_length=15)
    old_status = None
    def __str__ (self):
        return self.address
    def __init__(self, *args, **kwargs):
        super(Order, self).__init__(*args, **kwargs)
        self.old_status = self.status
    def save(self, *args, **kwargs):
        if self.old_status == None:
            self.old_status = 'pending'
        elif self.old_status != self.status:
            if self.status == 'approved' and self.old_status == 'pending':
                message = f"Yeni sifaris var http://api.purplecakeboutique.az/admin/api/order/{self.id}/change/"
                sendemail("contact@purplecakeboutique.az", message)
        super(Order, self).save(*args, **kwargs)
    class Meta:
        verbose_name = "Sifaris"
        verbose_name_plural = "Sifaris"

class OrderProduct(models.Model):
    order = models.ForeignKey('Order', on_delete=models.CASCADE)
    product = models.CharField(max_length=31, blank=True, null=True)
    quantity = models.IntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    url = models.URLField(max_length=255, blank=True, null=True)
    def __str__(self):
        return f'{self.quantity} x {self.content_object}'
    def save(self, *args, **kwargs):
        model = self.content_object._meta.object_name.lower()
        self.url = f'http://api.purplecakeboutique.az/admin/api/{model}/{self.content_object.id}/change/'
        self.product = self.content_object.name
        super(OrderProduct, self).save(*args, **kwargs)
