from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import stock
from .seralizers import stockSerializer

# list all stocks or create a new one
#stocks/
class stockList(APIView):

    def get(self, request):
        stocks = stock.objects.all()
        serializer = stockSerializer(stock, many=True)
        return Response(serializer.data)

    def post(self):
        pass