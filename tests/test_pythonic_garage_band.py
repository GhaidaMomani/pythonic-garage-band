from pythonic_garage_band import Musician, Guitarist, Drummer, Bassist, Band, read_file

def test_guitarist_role():
    expected = 'Guitarist'
    actual = Guitarist('Guitarist', 'guitar').role
    assert expected == actual

def test_guitarist_instrument():
    expected = 'guitar'
    actual = Guitarist('Guitarist', 'guitar').instrument
    assert expected == actual

def test_guitarist_str():
    expected = 'I am a Guitarist'
    actual = Guitarist('Guitarist', 'guitar').__str__()
    assert expected == actual

def test_guitarist_repr():
    assert 'Guitarist' == Guitarist('Guitarist', 'guitar').__repr__()

def test_guitarist_get_instrument():
    assert 'guitar' == Guitarist('Guitarist', 'guitar').get_instrument()

def test_guitarist_play_solo():
    assert 'Guitarist is playing solo on the guitar' == Guitarist('Guitarist', 'guitar').play_solo()

def test_drummer_play_solo():
     assert 'Drummer is playing solo on the drums' == Drummer('Drummer', 'drums').play_solo()

def test_guitarist_str():
    assert 'I am a Bassist' == Bassist('Bassist', 'bass').__str__()

def test_musicians_members():
    Musician.members = []
    guitarist = Guitarist('Guitarist', 'guitar')
    bassist = Bassist('Bassist','bass')
    drummer = Drummer('Drummer', 'drums')
    assert [guitarist, bassist, drummer] == Musician.members

band_data = Band.create_from_data(read_file("band.txt"))
new_band = Band(band_data[0], band_data[1])

def test_Band_instance():

    assert new_band.name == "Random Group"

def test_Band_play_solos():

    assert new_band.play_solos() == "Guitarist is playing solo on the  guitar\nDrummer is playing solo on the  drums\nDrummer is playing solo on the  drums\nDrummer is playing solo on the  drums\nBassist is playing solo on the  bass\nGuitarist is playing solo on the  guitar"

def test_Band_str():
    assert str(new_band)== 'We are the Random Group'

def test_Band_repr():
    assert repr(new_band)== 'This is the Random Group'

def test_Band_to_list():
    assert Band.to_list() == [Band.all[0], Band.all[1], Band.all[2]]

def test_Band_create_from_data():
    new_band_data = Band.create_from_data(read_file("band.txt"))
    assert  new_band_data[0]== "Random Group"
    assert  len(new_band_data[1]) == 6

# Edge case when given role from data doesn't have class for it

def test_role_doesn_exist():

    assert Band.create_from_data(read_file("band_test.txt")) == "Vocalist doesn't exists in DB"