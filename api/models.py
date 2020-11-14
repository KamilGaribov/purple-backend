from django.db import models
from django.utils.translation import gettext as _
from django.utils.html import mark_safe

class Cake(models.Model):
    name = models.CharField(max_length=63)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, default=5.90)
    discount = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, blank=True, null=True, default=7)
    ingredient = models.CharField(max_length=511, blank=True, null=True)
    weight = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='', blank=True, null=True)
    similar1 = models.ForeignKey('Cake', on_delete=models.SET_NULL, blank=True, null=True)
    similar2 = models.ForeignKey('Cake', on_delete=models.SET_NULL, blank=True, null=True)
    similar3 = models.ForeignKey('Cake', on_delete=models.SET_NULL, blank=True, null=True)
    similar4 = models.ForeignKey('Cake', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
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