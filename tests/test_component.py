import pytest
from src.app import app
import json


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_predict_endpoint(client):
    response = client.post('/predict',
                           data=json.dumps({'text': 'mlops'}),
                           content_type='application/json')

    assert response.status_code == 200
    data = response.get_json()
    assert 'prediction' in data
    assert 'bucket' in data