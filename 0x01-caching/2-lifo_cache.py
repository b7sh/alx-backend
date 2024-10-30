#!/usr/bin/env python3
'''
a class LIFOCache that inherit
s from BaseCaching and is a caching system
'''
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''
    You must use self.cache_data - dictionary
    from the parent class BaseCaching
    '''
    def __init__(self):
        '''
        Initialize
        '''
        super().__init__()
        self.keys = []

    def put(self, key, item):
        '''
        Must assign to the dictionary self.cache_data
        the item value for the key key
        '''
        if key is not None and item is not None:
            self.cache_data[key] = item
            if key not in self.keys:
                self.keys.append(key)
            else:
                self.keys.append(self.keys.pop(self.keys.index(key)))
            if len(self.keys) > BaseCaching.MAX_ITEMS:
                discard = self.keys.pop(-2)
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
