from requests import Response, post, get

from tests.test_data.API_tests_smoke_data import post_creation_validation


def test_post_existence_validation():
    response: Response = get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200


def test_post_creation_validation():
    response: Response = post("https://jsonplaceholder.typicode.com/posts",
                              json=post_creation_validation)
    assert response.status_code == 201
