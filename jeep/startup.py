''' An object that runs on startup.
'''

from syslog import syslog

class StartUp(object):
    ''' The StartUp object is initiated once the jeep boots.
    '''
    
    def __init__(self):
        syslog('The jeep has started')
        self.running = True
