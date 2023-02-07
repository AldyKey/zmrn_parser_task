from datetime import datetime, timedelta

from . import models as models

def get_dates(company_symbol):
    # Function to get "date_from" and "date_to" values
    news_exist = models.CompanyNews.objects.filter(news_ticker_name=company_symbol) # This will check if news for the ticker exists
    current_datetime = datetime.today()
    # If arctiles do not exist the "date_from" will be 30 days before, and "date_to" will be 20 days before
    if not news_exist:
        date_from_raw = current_datetime - timedelta(30)
        date_from = date_from_raw.strftime('%Y-%m-%d')
        date_to_raw = current_datetime - timedelta(20)
        date_to = date_to_raw.strftime('%Y-%m-%d')
    # If news exist, there is filter that will get the latest article's date, and it will be the value of "date_from" 
    # And "date_to" will be 10 days ahead
    elif news_exist:
        last_article = models.CompanyNews.objects.filter(news_ticker_name=company_symbol).order_by("news_datetime").last()
        date_from_raw = last_article.news_datetime
        date_from = date_from_raw.strftime('%Y-%m-%d')
        date_to_raw = last_article.news_datetime + timedelta(10)
        # If date_to_raw will be bigger than current_datetime then date_to will be current_datetime
        if date_to_raw > current_datetime:
            date_to = current_datetime.strftime('%Y-%m-%d')
        else:
            date_to = date_to_raw.strftime('%Y-%m-%d')
    return date_from, date_to
