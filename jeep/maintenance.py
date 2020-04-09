'''A class for scheduling maintenance on the jeep.
'''

from datetime import datetime

class Maintenance:
    ''' A base maintenance class.
    '''

    def __init__(self):
        self.has_ran = False
        self.label = u'Maintenance'
        self.assignee = 'zachseifts'
        self.repo = 'zachseifts/jeeps'

    def create(self):
        ''' This function creates an issue in the repo
        '''
        self.has_ran = True


class GreaseJob(Maintenance):
    ''' This class schedules a grease job for the jeep.
    '''

    def __init__(self, **kwargs):
        ''' Default constructor for the GreaseJob class.

        Parameters
        ----------
        account_token: str
            A github account token.
        '''
        self.account_token = kwargs.get('account_token', False)
        self.title = u'Monthly: Grease job and inspection'
        self.body = u'It is time to check on the jeep.'
        super().__init__()
        self.create()

