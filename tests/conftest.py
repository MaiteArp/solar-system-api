import pytest 
from app import create_app 
from app import db
from app.model.planet import Planet


@pytest.fixture 
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()

        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def adds_two_planets(app):
#Arrange
    mercury = Planet(name="mercury",
    description="First from the sun",
    distance_from_sun=29.839
    )
    venus = Planet(name="venus",
    description="Second from the sun",
    distance_from_sun=67.04
    )
    db.session.add_all([mercury, venus])
    db.session.commit()

