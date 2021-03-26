import redis
from django.conf import settings
from .models import Product


r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIT_PORT, db=settings.REDIS_DB)
