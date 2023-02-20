from pytest_voluptuous import S

from schemas.user import users_list_schema


def test_get_list_users_ok(reqres_in):
    response = reqres_in.get('/api/users', params={"page": 2})

    assert response.status_code == 200
    assert S(users_list_schema) == response.json()
    assert response.json()["data"][0]["email"] == "michael.lawson@reqres.in"
