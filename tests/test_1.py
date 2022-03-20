import json

def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    expected = 1
    assert expected == json.loads(res.get_data(as_text=True))['status_code']

def test_index2(app, client):
    res = client.get('/playground')
    assert res.status_code == 200
    expected = 1
    assert expected == json.loads(res.get_data(as_text=True))['status_code']
