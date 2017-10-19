import unittest

from jeep import Location
from jeep import StartUp

class TestLocationClass(unittest.TestCase):
    ''' A test class for testing the Location.
    '''
    
    def test_init(self):
        ''' Test the init process for setting up a new Location.
        '''
        location = Location(longitude=123.1234, latitude=123.1234)
        self.assertEquals(location.longitude, 123.1234)
        self.assertEquals(location.latitude, 123.1234)
        
    def test_startup(self):
        ''' Test the Startup class.
        '''
        startup = StartUp()
        self.assertTrue(startup.running)


if __name__ == '__main__':
    unittest.main()
