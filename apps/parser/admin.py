from django.contrib import admin

from . models import CompanyNews

@admin.register(CompanyNews)
class CompanyNewsAdmin(admin.ModelAdmin):
    list_display = ['id','news_id', 'news_datetime', 'news_ticker_name', 'news_headline']
    search_fields = ['news_id', "news_ticker_name", "news_datetime"]
    readonly_fields = ['news_datetime']
    ordering = ('-news_datetime',)