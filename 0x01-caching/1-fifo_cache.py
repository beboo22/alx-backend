#!/usr/bin/python3
""" FIFOCache class
"""
from collections import deque
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    '''A class `FIFOCache` that inherits from
       `BaseCaching` .
    '''
    def __init__(self):
        super().__init__()
        self.order_of_arrival = deque()

    def put(self, key, item):
        '''assign to the dictionary `self.cache_data` the
           `item` value for the key `key`
        '''
        if key is not None or item is not None:
            if key not in self.cache_data and item not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    if key is None or item is None:
                        pass
                    else:
                        old_key = self.order_of_arrival.popleft()
                        print("DISCARD: {}".format(old_key))
                        del self.cache_data[old_key]
            self.cache_data[key] = item
            self.order_of_arrival.append(key)
        else:
            pass

    def get(self, key):
        '''return the value in `self.cache_data` linked to `key`
        '''
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
