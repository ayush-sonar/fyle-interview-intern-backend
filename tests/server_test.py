from core.libs import helpers


def test_root(client):
    response = client.get('/')
    time=helpers.get_utc_now()
    assert response.status_code == 200
    assert response.json['status'] == 'ready'
