import unittest

from jeep.location import Location
from jeep.startup import StartUp

class TestLocationClass(unittest.TestCase):
    ''' A test class for testing the Location.
    '''

    def test_init(self):
        ''' Test the init process for setting up a new Location.
        '''
        lat = 12.1234
        lon = 12.1234
        location = Location(latitude=lat, longitude=lon)
        self.assertEqual(location.latitude, lat)
        self.assertEqual(location.longitude, lon)

    def test_startup(self):
        ''' Test the Startup class.
        '''
        startup = StartUp()
        self.assertTrue(startup.running)


if __name__ == '__main__':
    unittest.main()
