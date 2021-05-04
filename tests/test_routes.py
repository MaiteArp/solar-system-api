

# get all planets and return empty list w/ no planets 

def test_get_all_planets_with_no_records(client):
    #act
    response = client.get("/planets")
    response_body = response.get_json()

    #assert 
    assert response.status_code == 200
    assert response_body[0] == []

# get planets with id number
def test_get_planet_by_id(client, adds_two_panets):
    #Act
    response = client.get("/planets/1")
    response_body = response.get_json()
    print(response_body)
    #Assert
    assert response.status_code == 200
    assert response_body == {"name": "mercury",
    "description": "First from the sun",
    "distance_from_sun": 29.839,
    "id": 1
    }

#get planets with empty db
def test_get_planets_empty_db(client):
    #Act
    response = client.get("/planets/1")
    response_body = response.get_json()
    #Assert
    assert response.status_code == 404
    assert response_body["success"] == False


# get planets with populated db returns list
def test_get_planets_with_records(client, adds_two_panets):
    #Act
    response = client.get("/planets")
    response_body = response.get_json()
    #Assert
    assert response.status_code == 200
    assert len(response_body) == 2
    assert response_body[0][0] == {"name": "mercury",
    "description": "First from the sun",
    "distance_from_sun": 29.839,
    "id": 1
    }
    assert response_body[0][1] == {"name": "venus",
    "description": "Second from the sun",
    "distance_from_sun": 67.04,
    "id": 2
    }

# post planets with json return body posts planet 201
def test_post_planet(client):
    #Act
    post = client.post('/planets', json={"name": "mercury",
    "description": "First from the sun",
    "distance_from_sun": 29.839,
    })
    response_body = post.get_json()
    #Assert
    assert post.status_code == 201
    assert response_body["Success"] == True