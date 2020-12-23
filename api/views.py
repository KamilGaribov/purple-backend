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
certificate_folder = os.path.join(settings.BASE_DIR, 'certificates')
urllib3.disable_warnings()


class Test(APIView):
    permission_classes = [
        permissions.AllowAny
    ]

    def post(self, request):
        print("__________request.body")
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        content = body['data']
        print("body: ", body)
        print("ad: ", content['name'])
        print("soyad: ", content['surname'])
        print("body[amount]: ", body['amount'])


        amount = body['amount'] * 100
        print("amount::-=-=-: ", amount)
        # qiymetler cemi
        description = f'Purple Cake Boutique'
        headers = {"Content-Type": "application/xml"}
        url = "https://e-commerce.kapitalbank.az:5443/Exec"
        cert = f"{certificate_folder}/purple.crt"
        key = f"{certificate_folder}/purple.key"
        payload = f"""<?xml version="1.0" encoding="UTF-8"?>
        <TKKPG>
        <Request>
            <Operation>CreateOrder</Operation>
            <Language>AZ</Language>
            <Order>
                <OrderType>Purchase</OrderType>
                <Merchant>E1000010</Merchant>
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
        print('response___: ', response)
        print("response.cookies___: ", response.cookies)
        print("response.content__: ", response.content)
        context = {"result": "success"}
        xml_response = xmlET.fromstring(response.content)
        for i in xml_response.iter("*"):
            context[i.tag] = i.text
        if context['Status'] == '00':
            print("content.surname: ", content['surname'])
            order = Order.objects.create(orderid=context['OrderID'])
            order.name = content['name']
            order.surname = content['surname']
            order.email = content['email']
            order.amount = amount/100
            order.address = content['address']
            order.address2 = content['address2']
            print("contex.id: ", context['OrderID'])
            print("context.[oderid] ", context['OrderID'])
            # order.orderid = context['OrderID']
            order.sessionid = context['SessionID']
            print("_____will save")
            order.save()
            url2 = 'https://e-commerce.kapitalbank.az/index.jsp?ORDERID=' + context['OrderID'] + '&SESSIONID=' + context['SessionID']
            # orderid = context.OrderID
            # sessionid = context.SessionID
            return Response({"Status": "00", "url": url2}, status=status.HTTP_200_OK)
        return Response({"Status": "30"}, status=status.HTTP_200_OK)

# @method_decorator(csrf_exempt, name='dispatch')
@csrf_exempt
def MakeOrder(request):
    if request.method == 'POST':
        print("request__: ", request)
        print(request.POST)
        context = {}
        data = request.POST.get("xmlmsg")
        print("xmlmsg___: ", data)
        xml_response = xmlET.fromstring(data)
        for i in xml_response.iter("*"):
            context[i.tag] = i.text
        print("context_________: ", context)
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


# def create_payment(language, reservation_id, amount):
#     try:
#         reservation_id = 123
#         amount = 12
#         description = f"Payment For Order {reservation_id}"
#         headers = {"Content-Type": "application/xml"}
#         url = "https://e-commerce.kapitalbank.az:5443/Exec"
#         amount = amount * 100
#         cert = f"{certificate_folder}/purple.crt"
#         key = f"{certificate_folder}/purple.key"
#         payload = f"""<?xml version="1.0" encoding="UTF-8"?>
#         <TKKPG>
#         <Request>
#             <Operation>CreateOrder</Operation>
#             <Language>AZ</Language>
#             <Order>
#                 <OrderType>Purchase</OrderType>
#                 <Merchant>E1000010</Merchant>
#                 <Amount>{amount}</Amount>
#                 <Currency>944</Currency>
#                 <Description>{description}</Description>
#                 <ApproveURL>http://purplecakeboutique.az/</ApproveURL>
#                 <CancelURL>http://purplecakeboutique.az/</CancelURL>
#                 <DeclineURL>http://purplecakeboutique.az/</DeclineURL>
#             </Order>
#         </Request>
#         </TKKPG>"""
#         # session = requests.session()
#         response = requests.post(
#             url,
#             data=payload,
#             headers=headers,
#             cert=(cert, key),
#             verify=False,
#         )
#         print('response___: ', response)
#         print("response.cookies___: ", response.cookies)
#         print("response.context__: ", response.content)
#         context = {"result": "success"}
#         # xml_response = ElementTree.fromstring(response.content)
#         # for i in xml_response.iter("*"):
#         #     # print(i.text)
#         #     context[i.tag] = i.text
#         return context
#     except Exception as er:
#         print("error__: ", er)


# @method_decorator(csrf_exempt, name='dispatch')
# class PaymentReturnURL(TemplateView):
#     success_url = reverse_lazy('after_payment')

#     def get_success_url(self):
#         # self.request.session['after_payment'] = True
#         return self.success_url

#     def get(self, request, *args, **kwargs):
#         return redirect(self.get_success_url())

#     def post(self, request, *args, **kwargs):
#         context = {}
#         data = self.request.POST.get("xmlmsg")
#         # print(data,"xmlmsg")
#         xml_response = ElementTree.fromstring(data)
#         for i in xml_response.iter("*"):
#             context[i.tag] = i.text
#         status = context.get("OrderStatus")
#         id = context.get("OrderDescription").split(' ')[3]
#         order_id = context.get("OrderID")
#         amount = context.get("PurchaseAmountScr")
#         card = context.get("PAN")
#         if status == "APPROVED":
#             reservation = Reservation.objects.get(id=id)
#             if reservation:
#                 payment = Payment.objects.create(patient=reservation.patient,
#                                                  doctor=reservation.doctor,
#                                                  reservation=reservation,
#                                                  order_id=order_id,
#                                                  amount=amount,
#                                                  card=card)
#                 payment.save()
#                 reservation.status = "Finished"
#                 reservation.save()
#             print("APPROVED")
#             # request.session['after_payment'] = True
#             return redirect("after_payment")
#         elif status == "CANCELED":
#             print("CANCELL")
#             return redirect("index")
#         elif status == "DECLINED":
#             print("DECLINED")
#             return redirect("after_error_payment")
#         else:
#             print("ELSEEEE")
#             return redirect("login")



# @for_patient_only
# def make_payment(request,reservation_id,amount):
#     # payment = create_payment('AZ', 300, 1)
#     user, _ = get_current_user(request.user.email)
#     reservation = Reservation.objects.filter(id=reservation_id,status="Pending").last()
#     if reservation and reservation.patient == user:
#         payment = create_payment('AZ', reservation_id, amount)
#         payment_url = payment.get("URL") + "?ORDERID=" + payment.get("OrderID") + "&SESSIONID=" + payment.get(
#             "SessionID")
#         # self.add_payment_event('pre-auth', total_incl_tax.incl_tax)
#         return HttpResponseRedirect(payment_url)
#     else:
#         return HttpResponse(status=403)




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
    queryset = Vitrin.objects.filter(publish=True)
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = VitrinSerializer


class MarsipanApi(viewsets.ModelViewSet):
    queryset = Marsipan.objects.filter(publish=True)
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = MarsipanSerializer


class FlowerApi(viewsets.ModelViewSet):
    queryset = Flower.objects.filter(publish=True)
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FlowerSerializer


class XoncaApi(viewsets.ModelViewSet):
    queryset = Xonca.objects.filter(publish=True)
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
        vitrin = Vitrin.objects.filter(homepage=True).order_by(
            '?')[0: HomePageProduct.objects.all()[0].vitrin]
        marsipan = Marsipan.objects.filter(homepage=True).order_by(
            '?')[0: HomePageProduct.objects.all()[0].marsipan]
        flower = Flower.objects.filter(homepage=True).order_by(
            '?')[0: HomePageProduct.objects.all()[0].flower]
        xonca = Xonca.objects.filter(homepage=True).order_by(
            '?')[0: HomePageProduct.objects.all()[0].xonca]
        list = chain(vitrin, marsipan, flower, xonca)
        if list:
            return list
        else:
            return []
