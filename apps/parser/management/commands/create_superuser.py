from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from django.conf import settings

class Command(BaseCommand):
   help = 'Create superuser if it does not exist'

   def handle(self, *args, **options):
      if not User.objects.filter(username='admin').exists():
         User.objects.create_superuser(settings.SUPERUSER_USERNAME, settings.SUPERUSER_MAIL, settings.SUPERUSER_PASSWORD)