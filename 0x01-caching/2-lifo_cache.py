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
                print("DISCARD:", last_key)
        self.cache_data[key] = item
        self.cache_data.move_to_end(key, last=True)
    
    def get(self, key):
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None

# def put(self, key, item):
    #     """ Adds an item to the cache using LIFO algorithm """
    #     if key is not None and item is not None and key not in self.cache_data:
    #         if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
    #             last_key = list(self.cache_data.keys())[-1]
    #             del self.cache_data[last_key]
    #             print(f"DISCARD: {last_key}")
    #     elif key is not None and item is not None and key  in self.cache_data:
    #         print("DISCARD: {}".format(key))
    #         del self.cache_data[key]
    #     self.cache_data[key] = item
    
    
    # def put(self, key, item):
    #     if key is not None and item is not None:
    #         if key not in self.cache_data:
    #             if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
    #                 recent_key = self.order_of_arrival.pop()
    #                 print("DISCARD: {}".format(recent_key))
    #                 del self.cache_data[recent_key]
                
    #         else:
    #             print("DISCARD: {}".format(key))
    #             del self.cache_data[key]
    #         self.order_of_arrival.append(key)
    #         self.cache_data[key] = item
    
        # if key is not None and item is not None:
        #     if key not in self.cache_data:
        #         if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
        #             recent_key, _ = self.cache_data.popitem()
        #             print("DISCARD: {}".format(recent_key))
        #             del self.cache_data[recent_key]
                
        #     else:
        #         print("DISCARD: {}".format(key))
        #         del self.cache_data[key]
        #     self.order_of_arrival.append(key)
        #     self.cache_data[key] = item
