'''A class for scheduling maintenance on the jeep.
'''

from github import Github

class Maintenance:
    ''' A base maintenance class.
    '''

    def __init__(self):
        self.assignee = 'zachseifts'
        self.repo_name = 'zachseifts/jeeps'

    def create(self):
        ''' This function creates an issue in the repo
        '''
        self.repo.create_issue(
            title=self.title,
            body=self.body,
            labels=[self.label],
            assignee=self.assignee)


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

    def run(self):
        if self.account_token:
            self.github = Github(self.account_token)
            self.repo = self.github.get_repo(self.repo_name)
            self.label = self.repo.get_label('Maintenance')
            self.create()

