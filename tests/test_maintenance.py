from jeep.maintenance import GreaseJob

def test_greasejob():
    ''' This test tests the GreaseJob object.
    '''
    g = GreaseJob()
    assert g.label == 'Maintenance'
    assert g.assignee == 'zachseifts'
    assert g.repo == 'zachseifts/jeeps'
    assert g.title == 'Monthly: Grease job and inspection'
    assert g.body == 'It is time to check on the jeep.'
    assert g.has_ran
