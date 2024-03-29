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

BACKLINK_TYPES = [
    ('from_facebook', 'from_facebook'),
    ('from_instagram', 'from_instagram'),
    ('from_oxu_az', 'from_oxu_az'),
    ('to_facebook', 'to_facebook'),
    ('to_instagram', 'to_instagram'),
]

class Vitrin(models.Model):
    name = models.CharField(max_length=63, unique=True)
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
        verbose_name_plural = "Vitrin"


class VitrinCategory(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Vitrin kateqoriyaları"


class Marsipan(models.Model):
    name = models.CharField(max_length=63, unique=True)
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
        verbose_name_plural = "Marsipan"


class MarsipanCategory(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Marsipan kateqoriyaları"

class Flower(models.Model):
    name = models.CharField(max_length=63, unique=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, default=12.00)
    discount = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey(
        'FlowerCategory', on_delete=models.SET_NULL, blank=True, null=True, default=4)
    ingredient = models.CharField(max_length=511, blank=True, null=True)
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
        verbose_name_plural = "Gül"


class FlowerCategory(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Gül kateqoriyaları"

class Xonca(models.Model):
    name = models.CharField(max_length=63, unique=True)
    price = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True, default=12.00)
    discount = models.DecimalField(
        max_digits=6, decimal_places=2, blank=True, null=True)
    category = models.ForeignKey(
        'XoncaCategory', on_delete=models.SET_NULL, blank=True, null=True, default=4)
    ingredient = models.CharField(max_length=511, blank=True, null=True)
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
        verbose_name_plural = "Xonca"


class XoncaCategory(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Xonça kateqoriyaları"


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
        verbose_name_plural = "Mektublar"


class HomePageProduct(models.Model):
    vitrin = models.IntegerField(default=2)
    marsipan = models.IntegerField(default=2)
    flower = models.IntegerField(default=2)
    xonca = models.IntegerField(default=2)
    def __str__(self):
        return "Say"
    class Meta:
        verbose_name = "Ancaq 1-ci say işləyir"
        verbose_name_plural = "Ana səhifə sayları"

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
                sendemail("dianaguven@hotmail.com", message)
                sendemail("halimecoskunn@hotmail.com", message)
                sendemail("aqilbalagozov@gmail.com", message)
                sendemail("nigarmalikzade@gmail.com", message)
        super(Order, self).save(*args, **kwargs)
    class Meta:
        verbose_name_plural = "Sifarislər"

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


class SocialMedia(models.Model):
    to_facebook = models.IntegerField(blank=True, null=True, default=0)
    to_instagram = models.IntegerField(blank=True, null=True, default=0)
    from_facebook = models.IntegerField(blank=True, null=True, default=0)
    from_instagram = models.IntegerField(blank=True, null=True, default=0)
    from_oxu_az = models.IntegerField(blank=True, null=True, default=0)
    def __str__(self):
        return '1 ədəd olmalıdır'
    class Meta:
        verbose_name_plural = "Sosial medya backlink'ləri"
    def save(self, *args, **kwargs):
        self.from_facebook = Backlink.objects.filter(action='from_facebook').count()
        self.from_instagram = Backlink.objects.filter(action='from_instagram').count()
        self.from_oxu_az = Backlink.objects.filter(action='from_oxu_az').count()
        self.to_facebook = Backlink.objects.filter(action='to_facebook').count()
        self.to_instagram = Backlink.objects.filter(action='to_instagram').count()
        super(SocialMedia, self).save(*args, **kwargs)


class Backlink(models.Model):
    action = models.CharField(choices=BACKLINK_TYPES, max_length=15)
    ip = models.CharField(max_length=31)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.ip + " " + self.action
    class Meta:
        verbose_name_plural = "Backlink IP'ləri"