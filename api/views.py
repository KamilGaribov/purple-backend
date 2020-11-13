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

class NextAppView(View):

    def get(self, request):
        try:
            with open(os.path.join(settings.NEXT_APP, 'out', 'index.js')) as file:
                return HttpResponse(file.read())
        except :
            return HttpResponse(
                """
                index.html not found ! build your Next app !!
                """,
                status=501,
            )



# class StadionApi(ReadOnlyModelViewSet):
class CakeApi(viewsets.ModelViewSet):
    queryset = Cake.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CakeSerializer

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