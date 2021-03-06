from django.core.cache import cache
from django.conf import settings


def cache_update(sender, **kwargs):
    item = kwargs.get('instance')
    cache.set(item.cache_key, item, settings.CACHE_TIMEOUT)


def cache_evict(sender, **kwargs):
    item = kwargs.get('instance')
    cache.delete(item.cache_key)
