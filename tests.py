import unittest

from jeep import Location

class TestLocationClass(unittest.TestCase):
    ''' A test class for testing the Location.
    '''
    
    def test_init(self):
        ''' Test the init process for setting up a new Location.
        '''
        location = Location()
        self.assertIsNone(location.longitude)
        self.assertIsNone(location.latitude)


if __name__ == '__main__':
    unittest.main()
