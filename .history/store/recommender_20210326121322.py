import redis
from django.conf import settings
from .models import Product


r = redis.Redis()
