import unittest

from jeep.location import Location
from jeep.startup import StartUp
from jeep.maintenance import GreaseJob

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


class TestMaintenance(unittest.TestCase):

    def test_greasejob(self):
        ''' Tests the greasejob class
        '''
        g = GreaseJob()
        self.assertEqual(g.label, 'Maintenance')
        self.assertEqual(g.assignee, 'zachseifts')
        self.assertEqual(g.repo, 'zachseifts/jeeps')
        self.assertEqual(g.title, 'Monthly: Grease job and inspection')
        self.assertEqual(g.body, 'It is time to check on the jeep.')
        self.assertTrue(g.has_ran)


if __name__ == '__main__':
    unittest.main()
