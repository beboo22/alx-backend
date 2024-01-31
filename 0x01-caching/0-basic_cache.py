#!/usr/bin/python3
""" FIFOCache class
"""
from BaseCaching import BaseCaching


class BasicCache(BaseCaching):
    """ FIFOCache class
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
