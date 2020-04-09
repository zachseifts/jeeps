from jeep.location import Location

def test_location():
    ''' This test tests the Location object.
    '''

    lat = 12.1234
    lon = 12.1234
    location = Location(latitude=lat, longitude=lon)
    assert location.latitude == lat
    assert location.longitude == lon
