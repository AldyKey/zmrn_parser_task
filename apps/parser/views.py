from django.shortcuts import render
from django.conf import settings

from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from datetime import datetime, timedelta
import datetime as dt

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
        date_to_raw = request.query_params.get("date_to", "") 

        if date_from_raw and date_to_raw:
            date_from = utils.validate_date(date_from_raw) #validating string dates
            date_to = utils.validate_date(date_to_raw)
            
            if not date_from or not date_to:
                return Response(data="The dates should be in format YYYY-MM-DD", status=status.HTTP_400_BAD_REQUEST)
            data = models.CompanyNews.objects.filter(news_datetime__range=(date_from, date_to), news_ticker_name=path_name).order_by('news_datetime')

        elif not date_from_raw and not date_to_raw:
            # If User did not specified the dates, then User will get all the articles
            data = models.CompanyNews.objects.filter(news_ticker_name=path_name).order_by('news_datetime')

        else:
            # If User specified only one of the parameters
            return Response(data="You should spicify two parameters: date_from and date_to", status=status.HTTP_400_BAD_REQUEST)
        
        if not data:
            if path_name not in settings.TICKERS:
                return Response(data="Sorry, there is no articles about this ticker", status=status.HTTP_404_NOT_FOUND)
            return Response(data="Sorry, there is no articles between these two dates", status=status.HTTP_400_BAD_REQUEST)

        # Pagination of the response
        page = self.paginate_queryset(data)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)