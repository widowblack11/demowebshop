from pytest_voluptuous import S

from schemas.user import add_user


def test_create_user_ok(reqres):
    body = {
    "name": "morpheus",
    "job": "leader"
}
    response = reqres.post('/api/users', data=body)
    assert response.status_code == 201
    assert S(add_user) == response.json()
    assert response.json()["name"] == "morpheus"


def test_create_user_without_job(reqres):
    body = {
        "name": "morpheus"
    }
    response = reqres.post('/api/users', data=body)
    assert response.status_code == 201
    assert S(add_user) == response.json()





