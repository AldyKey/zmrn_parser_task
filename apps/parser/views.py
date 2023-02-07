from django.shortcuts import render
from django.conf import settings

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from datetime import datetime, timedelta

from . import models as models
from . import classes as classes
from . import serializers as serializers
from . import utils as utils

class AllCompanyNewsViewSet(viewsets.ReadOnlyModelViewSet):
    # This viewset class is to get all the available news for all tickers
    queryset = models.CompanyNews.objects.all().order_by('-news_datetime')
    serializer_class = serializers.CompanyNewsSerializer
    pagination_class = classes.Pagination
    permission_classes = [permissions.AllowAny]

class CompanyNewsViewSet(viewsets.ReadOnlyModelViewSet):
    # This viewset class is to get news for a specific ticker
    serializer_class = serializers.CompanyNewsSerializer
    pagination_class = classes.Pagination
    permission_classes = [permissions.AllowAny]

    @action(detail=True, methods=['get'])
    def list(self, request, path_name=None, *args, **kwargs):
        # path_name is url path that will be passed by user
        # TSLA, AMZN and etc.
        date_from_raw = request.query_params.get("date_from", "") # string type date
        date_from = datetime.strptime(date_from_raw, "%Y-%m-%d") # converting the string date to datetime
        date_to_raw = request.query_params.get("date_to", "") 
        date_to = datetime.strptime(date_to_raw, "%Y-%m-%d")
        date_to = date_to + timedelta(days=1)

        # In case User has swapped the values of two parameters
        if date_from > date_to:
            return Response(data="You should swap values of 'date_from' and 'date_to'", status=status.HTTP_400_BAD_REQUEST)

        # If User types the identical dates for two parameters, then User will get articles of one day
        

        # If User added parameter 'date_from'
        if date_from:
            # If User added both parameters, 'date_to' and 'date_from'
            if date_to:
                checking = models.CompanyNews.objects.filter(news_datetime__range=(date_from, date_to), news_ticker_name=path_name).order_by('news_datetime')
            # In case User didnt add parameter 'date_to', then 'date_to' will be today's date
            else:
                date_to = datetime.today().strftime('%Y-%m-%d')
                checking = models.CompanyNews.objects.filter(news_datetime__range=(date_from, date_to), news_ticker_name=path_name).order_by('news_datetime')
        # If User didnt add any parameters, then it will output all the articles for specific ticker
        else:
            checking = models.CompanyNews.objects.filter(news_ticker_name=path_name).order_by('news_datetime')
        
        if not checking:
            if path_name not in settings.TICKERS:
                return Response(data="Sorry, there is no articles about this ticker", status=status.HTTP_404_NOT_FOUND)
            
            return Response(data="Sorry, there is no articles between these two dates", status=status.HTTP_400_BAD_REQUEST)

        # Pagination of the response
        page = self.paginate_queryset(checking)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)