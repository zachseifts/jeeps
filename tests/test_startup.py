from jeep.startup import StartUp

def test_startup():
    ''' This test tests the startup object.
    '''
    startup = StartUp()
    assert startup.running

