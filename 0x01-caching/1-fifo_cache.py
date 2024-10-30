#!/usr/bin/env python3
'''
Create a class FIFOCache that inherits
from BaseCaching and is a caching system
'''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''
    You must use self.cache_data - dictionary
    from the parent class BaseCaching
    You can overload def __init__(self): but
    don’t forget to call the parent init: super().__init__()
    '''
    def __init__(self):
        """
        Initiliaze
        """
        super().__init__()
        self.keys = []

    def put(self, key, item):
        '''
        ust assign to the dictionary self.cache_data
        the item value for the key key
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(0)
                del self.cache_data[discard]
                print('DISCARD: {:s}'.format(discard))

    def get(self, key):
        '''
        Must return the value in
        self.cache_data linked to key
        '''
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
