from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from women.serializers import WomenSerializer
from .models import Women

# Create your views here.


class Women_Api_View(APIView):
    def get(self):
        return Response({"title": "Angelina Jolie"})


# class Women_API_View(generics.ListAPIView):
#     queryset = Women.objects.all()
#     serializer_class = WomenSerializer
