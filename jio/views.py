from django.shortcuts import render
from .models import jiomodel
from .serializers import jioser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import views
from rest_framework import status

# Create your views here.

class jioshow(APIView):
    def get(self,r):
        orm=jiomodel.objects.all()
        ser=jioser(orm,many=True)
        return Response(ser.data,status=status.HTTP_200_OK)

    def post(self,r):
        ser=jioser(data=r.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_200_OK)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

class jioupdate(APIView):
    def put(self,r,pk):
        orm=jiomodel.objects.get(pk=pk)
        ser=jioser(orm,data=r.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_200_OK)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,r,pk):
        orm=jiomodel.objects.get(pk=pk)
        ser=jioser(orm)
        orm.delete()
        return Response(ser.data,status=status.HTTP_200_OK)


    def patch(self,r,pk):
        orm=jiomodel.objects.get(pk=pk)
        ser=jioser(orm,data=r.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_200_OK)
        return Response(ser.errors,status=status.HTTP_400_BAD_REQUEST)

class fetch(APIView):
    def get(self,r):
        #orm=jiomodel.objects.filter(recharge_amount__gt=1200)
        orm=jiomodel.objects.all().order_by('-recharge_amount')[1:2]
        ser=jioser(orm,many=True)
        return Response(ser.data,status=status.HTTP_200_OK)