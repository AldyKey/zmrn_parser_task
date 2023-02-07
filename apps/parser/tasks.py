from datetime import datetime
from django.db import transaction
from django.conf import settings

from celery import shared_task
from celery.utils.log import get_task_logger
import requests

from . import models as models
from . import utils as utils

logger = get_task_logger(__name__)

@shared_task
def parsing_news(company_symbol):
    # Periodic task that will be executed for each ticker
    # This task will send request to finnhub.io api and get news about the ticker between specific dates
    with transaction.atomic():
        date_from, date_to = utils.get_dates(company_symbol)
        try:
            response = requests.get(f"https://finnhub.io/api/v1/company-news?symbol={company_symbol}&from={date_from}&to={date_to}&token={settings.FINNHUB_TOKEN}")
            json_response = response.json()
            if response.status_code == 200:
                for new in json_response:
                    news_id = new.get("id")
                    checking = models.CompanyNews.objects.filter(news_id=news_id, news_ticker_name=company_symbol)
                    news_datetime_raw = new.get("datetime")
                    news_datetime = datetime.fromtimestamp(news_datetime_raw)
                    if not checking:
                        models.CompanyNews.objects.create(
                            news_category = new.get("category"),
                            news_datetime = news_datetime,
                            news_headline = new.get("headline"),
                            news_id = news_id,
                            news_image = new.get("image"),
                            news_ticker_name = new.get("related"),
                            news_source = new.get("source"),
                            news_summary = new.get("summary"),
                            news_url = new.get("url")
                        )
                print(f"{company_symbol} - News Added Between: {date_from} - {date_to}")
                return True
            else:
                print(json_response)
                return False
        except Exception as e:
            print(f"Error happened: {e}")
            return False