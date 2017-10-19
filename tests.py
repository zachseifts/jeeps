import unittest

from jeep import Location

class TestLocationClass(unittest.TestCase):
    ''' A test class for testing the Location.
    '''
    
    def test_init(self):
        ''' Test the init process for setting up a new Location.
        '''
        location = Location(longitude=123.1234, latitude=123.1234)
        self.assertEquals(location.longitude, 123.1234)
        self.assertEquals(location.latitude, 123.1234)


if __name__ == '__main__':
    unittest.main()
