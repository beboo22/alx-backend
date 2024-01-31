#!/usr/bin/python3
""" FIFOCache class
"""
from collections import deque, OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ FIFOCache class
    """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()
        self.order_of_arrival = deque()

    def put(self, key, item):
        """Adds an item in the cache.
        """
        if key is None or item is None:
            return
        if key not in self.cache_data:
            if len(self.cache_data) + 1 > BaseCaching.MAX_ITEMS:
                last_key, _ = self.cache_data.popitem(True)
                print("DISCARD: {}".formate(last_key))
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        '''return the value in `self.cache_data` linked to `key`
        '''
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
