from rest_framework import serializers

from . import models as models 

class CompanyNewsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "news_category",
            "news_datetime",
            "news_headline",
            "news_id",
            "news_image",
            "news_ticker_name",
            "news_source",
            "news_summary",
            "news_url"
        )
        model = models.CompanyNews