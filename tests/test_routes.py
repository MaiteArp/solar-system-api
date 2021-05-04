

# get all planets and return empty list w/ no planets 

def test_get_all_planets_with_no_records(client):
    #act
    response = client.get('/planets')
    response_body = response.get_json()

    #assert 
    assert response.status_code == 200
    print(response_body)
    assert response_body[0] == []

