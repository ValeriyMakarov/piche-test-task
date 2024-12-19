from requests import Response, post, get
from pytest import mark

from tests.test_data.API_tests_smoke_data import post_creation_validation
from core.utils import log


@mark.smoke
@mark.api
def test_post_existence_validation():
    log.info("1. Send get request.")
    response: Response = get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200, "Post doesn`t exist."


@mark.smoke
@mark.api
def test_post_creation_validation():
    log.info("1. Send post request.")
    response: Response = post("https://jsonplaceholder.typicode.com/posts",
                              json=post_creation_validation)
    assert response.status_code == 201, "Post was not created."
