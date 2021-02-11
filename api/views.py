from django.shortcuts import render
from rest_framework import *
from .serializer import *
from rest_framework import permissions, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
import os
from itertools import chain
from rest_framework.views import APIView
import requests
import urllib3
from urllib.request import urlopen
from django.http import HttpResponseRedirect
import xml.etree.ElementTree as xmlET
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import ssl
import socket
certificate_folder = os.path.join(settings.BASE_DIR, 'certificates')
urllib3.disable_warnings()
from pathlib import Path
import os
from django.conf import settings


class Test(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        content = body['data']
        basket = body['basket']
        amount = 0
        for i in basket:
            if i.split(":")[0] == 'vitrin':
                product = Vitrin.objects.get(id=i.split(":")[1])
                if product.discount:
                    amount += product.discount * int(basket[i])
                else:
                    amount += product.price * int(basket[i])
            elif i.split(":")[0] == 'marsipan':
                product = Marsipan.objects.get(id=i.split(":")[1])
                if product.discount:
                    amount += product.discount * int(basket[i])
                else:
                    amount += product.price * int(basket[i])
            elif i.split(":")[0] == 'flower':
                product = Flower.objects.get(id=i.split(":")[1])
                if product.discount:
                    amount += product.discount * int(basket[i])
                else:
                    amount += product.price * int(basket[i])
            elif i.split(":")[0] == 'xonca':
                product = Xonca.objects.get(id=i.split(":")[1])
                if product.discount:
                    amount += product.discount * int(basket[i])
                else:
                    amount += product.price * int(basket[i])
            
        amount *= 100
        description = f'Purple Cake Boutique'
        headers = {"Content-Type": "application/xml"}
        url = "https://e-commerce.kapitalbank.az:5443/Exec"
        cert = f"{certificate_folder}/purple.pem"
        key = f"{certificate_folder}/purple.key"
        password = "purple"
        payload = f"""<?xml version="1.0" encoding="UTF-8"?>
        <TKKPG>
        <Request>
            <Operation>CreateOrder</Operation>
            <Language>AZ</Language>
            <Order>
                <OrderType>Purchase</OrderType>
                <Merchant>E1020035</Merchant>
                <Amount>{amount}</Amount>
                <Currency>944</Currency>
                <Description>{description}</Description>
                <ApproveURL>http://api.purplecakeboutique.az/ordered/</ApproveURL>
                <CancelURL>http://purplecakeboutique.az/</CancelURL>
                <DeclineURL>http://purplecakeboutique.az/</DeclineURL>
            </Order>`
        </Request>
        </TKKPG>"""
        response = requests.post(
            url,
            data=payload,
            headers=headers,
            cert=(cert, key),
            verify=False,
        )
        context = {"result": "success"}
        xml_response = xmlET.fromstring(response.content)
        for i in xml_response.iter("*"):
            context[i.tag] = i.text
        if context['Status'] == '00':
            order = Order.objects.create(orderid=context['OrderID'])
            order.name = content['name']
            order.surname = content['surname']
            order.email = content['email']
            order.amount = amount/100
            order.address = content['address']
            order.address2 = content['address2']
            order.sessionid = context['SessionID']
            order.save()
            for i in basket:
                if i.split(":")[0] == 'vitrin':
                    product = Vitrin.objects.get(id=i.split(":")[1])
                elif i.split(":")[0] == 'marsipan':
                    product = Marsipan.objects.get(id=i.split(":")[1])
                elif i.split(":")[0] == 'flower':
                    product = Flower.objects.get(id=i.split(":")[1])
                elif i.split(":")[0] == 'xonca':
                    product = Xonca.objects.get(id=i.split(":")[1])
                order_product = OrderProduct.objects.create(order=order, content_object=product, object_id=i.split(":")[1], quantity=basket[i])
                order_product.save()
            url2 = 'https://e-commerce.kapitalbank.az/index.jsp?ORDERID=' + context['OrderID'] + '&SESSIONID=' + context['SessionID']
            return Response({"Status": "00", "url": url2}, status=status.HTTP_200_OK)
        return Response({"Status": "30"}, status=status.HTTP_200_OK)
    # def get(self, request):
    #     print("______________salam get request")
    #     sendemail("kamilgarib@gmail.com", "mektub1")
    #     sendemail("kamil129@inbox.ru", "mektub")
    #     sendemail("kamilgarib@gmail.com", "mektub2")
    #     return HttpResponse("404 not found")


@csrf_exempt
def MakeOrder(request):
    if request.method == 'POST':
        context = {}
        data = request.POST.get("xmlmsg")
        xml_response = xmlET.fromstring(data)
        for i in xml_response.iter("*"):
            context[i.tag] = i.text
        status = context.get("OrderStatus")
        order_id = context.get("OrderID")
        card = context.get("PAN")
        if Order.objects.get(orderid=order_id) and context.get("OrderStatus") == "APPROVED":
            order = Order.objects.get(orderid=order_id)
            order.status = 'approved'
            order.pan = card
            order.save()
            return redirect("http://purplecakeboutique.az/sebet/sifarisverildi/")
        return HttpResponse("Yenidən cəhd edin")
    return render(request, 'index.html')




# class StadionApi(ReadOnlyModelViewSet):
class VitrinApi(viewsets.ModelViewSet):
    queryset = Vitrin.objects.filter(publish=True)
    # permission_classes = [IsAuthenticated]
    serializer_class = VitrinSerializer
    http_method_names = ['get',]

class VitrinCategoryApi(viewsets.ModelViewSet):
    queryset = VitrinCategory.objects.all()
    serializer_class = VitrinCategorySerializer
    http_method_names = ['get', ]

class MarsipanApi(viewsets.ModelViewSet):
    queryset = Marsipan.objects.filter(publish=True)
    serializer_class = MarsipanSerializer
    http_method_names = ['get',]

class MarsipanCategoryApi(viewsets.ModelViewSet):
    queryset = MarsipanCategory.objects.all()
    serializer_class = MarsipanCategorySerializer
    http_method_names = ['get', ]

class FlowerApi(viewsets.ModelViewSet):
    queryset = Flower.objects.filter(publish=True)
    serializer_class = FlowerSerializer
    http_method_names = ['get',]

class FlowerCategoryApi(viewsets.ModelViewSet):
    queryset = FlowerCategory.objects.all()
    serializer_class = FlowerCategorySerializer
    http_method_names = ['get', ]

class XoncaApi(viewsets.ModelViewSet):
    queryset = Xonca.objects.filter(publish=True)
    serializer_class = XoncaSerializer
    http_method_names = ['get',]

class XoncaCategoryApi(viewsets.ModelViewSet):
    queryset = Xonca.objects.all()
    serializer_class = XoncaCategorySerializer
    http_method_names = ['get', ]

class CafeApi(viewsets.ModelViewSet):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer
    http_method_names = ['get',]


class ContactApi(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ContactSerializer


class HomePageProductCountApi(viewsets.ModelViewSet):
    queryset = HomePageProduct.objects.all()
    # permission_classes = [IsAuthenticated]
    serializer_class = HomePageProductSerializer
    http_method_names = ['get',]


class HomePageProductApi(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    serializer_class = VitrinSerializer
    http_method_names = ['get',]

    def get_queryset(self):
        vitrin = Vitrin.objects.filter(homepage=True, publish=True).order_by(
            '?')[0: HomePageProduct.objects.all()[0].vitrin]
        marsipan = Marsipan.objects.filter(homepage=True, publish=True).order_by(
            '?')[0: HomePageProduct.objects.all()[0].marsipan]
        flower = Flower.objects.filter(homepage=True, publish=True).order_by(
            '?')[0: HomePageProduct.objects.all()[0].flower]
        xonca = Xonca.objects.filter(homepage=True, publish=True).order_by(
            '?')[0: HomePageProduct.objects.all()[0].xonca]
        list = chain(vitrin, marsipan, flower, xonca)
        if list:
            return list
        else:
            return []
