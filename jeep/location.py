'''
A Location class.

This script keeps track of where the Jeep is.
'''

class Location:
    ''' A base location class.
    '''
    
    def __init__(self, **kwargs):
        self.longitude = kwargs.get('longitude', None)
        self.latitude = kwargs.get('latitude', None)

