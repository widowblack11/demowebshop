from pytest_voluptuous import S

from schemas.user import update_user


def test_update_info_about_user_ok(reqres):
    body = {
    "name": "morpheus",
    "job": "leader"
}
    response = reqres.patch('/api/users/2', data=body)
    assert response.status_code == 200
    assert S(update_user) == response.json()
    assert response.json()["name"] == "morpheus" and response.json()["job"] == "leader"


def test_update_info_about_user_when_two_user_job(reqres):
    body = {
    "name": "morpheus",
    "job": ["leader", "teacher"]
}
    response = reqres.patch('/api/users/2', data=body)
    assert response.status_code == 200
    assert response.json()["job"] == ["leader", "teacher"]