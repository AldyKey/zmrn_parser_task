from django.db import models

class CompanyNews(models.Model):
    news_category = models.CharField(
        max_length=50,
        verbose_name="Article Category",
        null=True,
        blank=True
    )
    news_datetime = models.DateTimeField(
        verbose_name="Published at",
        null=True,
        blank=True
    )
    news_headline = models.TextField(
        verbose_name="Article Headline",
        null=True,
        blank=True
    )
    news_id = models.IntegerField(
        verbose_name="Article ID",
        null=True,
        blank=True
    )
    news_image = models.CharField(
        max_length=500,
        verbose_name="Article Image",
        blank=True,
        null=True
    )
    news_ticker_name = models.CharField(
        max_length=16,
        verbose_name="Ticker",
        blank=True,
        null=True
    )
    news_source = models.CharField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Article Source"
    )
    news_summary = models.TextField(
        verbose_name="Article Summary",
        blank=True,
        null=True
    )
    news_url = models.URLField(
        max_length=500,
        blank=True,
        null=True,
        verbose_name="Article URL"
    )
    created_at = models.DateTimeField(
        verbose_name='Created at',
        auto_now_add=True,
        editable=False,
        db_index=True,
        null=True,
        blank=True
    )
    
    def __str__(self):
        return "[{}] - {}".format(self.news_id, self.news_ticker_name)
    
    class Meta:
        verbose_name = "Company Article"
        verbose_name_plural = "Company News"