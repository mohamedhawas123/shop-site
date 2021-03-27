import redis
from django.conf import settings
from .models import Product


r = redis.Redis(host=settings.REDIS_HOST, port=settings.REDIT_PORT, db=settings.REDIS_DB)


class Recommender(object):

    def get_product_key(self, id):
        return f"product:{id}:purchased with"
    
    def product_bought(self, products):
        products_ids = [p.id for p in products]
        for product_id in products_ids:
            for with_id in products_ids:
                if product_id != with_id:
                    r.zincrby(self.get_product_key(product_id), 1, with_id)
    

    def suggest_products_for(self, products, max_results=6):
        product_ids = [p.id for p in products]
        if len(products) ==1:
            suggestions = r.zrange(self.get_product_key(product_ids[0]), 0, -1, desc=True)[:max_results]
        
        else:
            flat_ids = ''.join([str(id) for id in product_ids ])
            tmp_key = f"tmp_{flat_ids}"
            keys = [self.get_product_key(id) for id in product_ids]
            r.zunionstore(tmp_key, keys)
            r.zrem(tmp_key, *product_ids)
            suggestions = r.zrange(tmp_key, 0, -1, desc=True)[:max_results]
            r.delete(tmp_key)
        
        suggested_products_ids = [int(d) for id in suggestion ]

        


