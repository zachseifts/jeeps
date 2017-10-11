#!/usr/bin/env python

'''
A Location class.

This script keeps track of where the Jeep is.

'''

class Location(object):
    ''' A location.
    '''
    
    def __init__(self. **kwargs):
        self.longitude = kwargs.get('longitude', None)
        self.latitude = kwargs.get('latitude', None)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
