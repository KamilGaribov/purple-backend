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
from urllib.request import urlopen


class Test(APIView):
    permission_classes = [
        permissions.AllowAny
    ]
    def get(self, request):
        # url = "https://e-commerce.kapitalbank.az:5443/Exec"
        url = "https://e-commerce.kapitalbank.az/index.jsp?"
        xml = """<?xml version="1.0" encoding="UTF-8"?>
        <TKKPG>
        <Request>
           <Operation>CreateOrder</Operation>
           <Language>RU</Language>
           <Order>
             <OrderType>Purchase</OrderType>
             <Merchant>E1000010</Merchant>
             <Amount>123456</Amount>
             <Currency>944</Currency>
             <Description>xxxxxxxx</Description>
             <ApproveURL>/testshopPageReturn.jsp</ApproveURL>
             <CancelURL>/testshopPageReturn.jsp</CancelURL>
             <DeclineURL>/testshopPageReturn.jsp</DeclineURL>
           </Order>
        </Request>
        </TKKPG>"""
        # headers = {
        #     # 'SOAPAction': "\"https://www.w3schools.com/xml/FahrenheitToCelsius\"",
        #     'Content-Type': "text/xml",
        #     'Cache-Control': "no-cache",
        # }
        # r = requests.get(url=url, data=xml)
        # print(r.text())
        headers = {'Content-Type': 'application/xml'} # set what your server accepts
        print(requests.post(url, data=xml, headers=headers).text)
        print("___test_______")
        return Response({"data": requests.post(url, data=xml, headers=headers).text}, status=status.HTTP_200_OK)
    




class NextAppView(View):

    def get(self, request):
        try:
            with open(os.path.join(settings.NEXT_APP, 'out', 'index.js')) as file:
                return HttpResponse(file.read())
        except:
            return HttpResponse(
                """
                index.html not found ! build your Next app !!
                """,
                status=501,
            )


# class StadionApi(ReadOnlyModelViewSet):
class VitrinApi(viewsets.ModelViewSet):
    queryset = Vitrin.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VitrinSerializer


class MarsipanApi(viewsets.ModelViewSet):
    queryset = Marsipan.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MarsipanSerializer


class FlowerApi(viewsets.ModelViewSet):
    queryset = Flower.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FlowerSerializer


class XoncaApi(viewsets.ModelViewSet):
    queryset = Xonca.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = XoncaSerializer


class CafeApi(viewsets.ModelViewSet):
    queryset = Cafe.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CafeSerializer


class ContactApi(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ContactSerializer

class HomePageProductCountApi(viewsets.ModelViewSet):
    queryset = HomePageProduct.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = HomePageProductSerializer


class HomePageProductApi(viewsets.ModelViewSet):    
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VitrinSerializer
    def get_queryset(self):
        vitrin = Vitrin.objects.filter(homepage=True).order_by('?')[0: HomePageProduct.objects.all()[0].vitrin]
        marsipan = Marsipan.objects.filter(homepage=True).order_by('?')[0: HomePageProduct.objects.all()[0].marsipan]
        flower = Flower.objects.filter(homepage=True).order_by('?')[0: HomePageProduct.objects.all()[0].flower]
        xonca = Xonca.objects.filter(homepage=True).order_by('?')[0: HomePageProduct.objects.all()[0].xonca]
        list = chain(vitrin, marsipan, flower, xonca)
        if list:
            return list
        else:
            return []
