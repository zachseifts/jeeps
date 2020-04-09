from jeep.maintenance import GreaseJob

def test_greasejob():
    ''' This test tests the GreaseJob object.
    '''
    g = GreaseJob(account_token='1')
    assert g.assignee == 'zachseifts'
    assert g.repo_name == 'zachseifts/jeeps'
    assert g.title == 'Monthly: Grease job and inspection'
    assert g.body == 'It is time to check on the jeep.'
