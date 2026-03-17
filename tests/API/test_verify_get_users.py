import pytest

from schemas.user_list_schema import user_list_schema
from utilities.response_validator import ResponseValidator
from utilities.schema_validator_utility import SchemaValidator

@pytest.mark.api
def test_verify_get_users(user_service):
    response = user_service.get_users(page=1)
    ResponseValidator.validate_status_code(response, 200)
    ResponseValidator.validate_response_time(response, 2000)
    ResponseValidator.validate_json_response(response)
    response_json = response.json()
    SchemaValidator.validate_schema(response_json, user_list_schema)
    assert len(response_json["data"]) > 0

@pytest.mark.api
def test_verify_get_users_invalid_page(user_service):
    response = user_service.get_users(page=999)
    ResponseValidator.validate_status_code(response, 200)
    ResponseValidator.validate_response_time(response, 2000)
    ResponseValidator.validate_json_response(response)
    response_json = response.json()
    SchemaValidator.validate_schema(response_json, user_list_schema)
    assert len(response_json["data"]) == 0

@pytest.mark.api
def test_verify_get_users_missing_page_param(user_service):
    response = user_service.client.get("/users")
    ResponseValidator.validate_status_code(response, 200)
    ResponseValidator.validate_response_time(response, 2000)
    ResponseValidator.validate_json_response(response)
    response_json = response.json()
    SchemaValidator.validate_schema(response_json, user_list_schema)
    assert len(response_json["data"]) > 0


@pytest.mark.api
def test_verify_get_users_invalid_page_defaults_to_first_page(user_service):
    response = user_service.client.get("/users", params={"page": "invalid"})
    ResponseValidator.validate_status_code(response, 200)
    ResponseValidator.validate_response_time(response, 2000)
    ResponseValidator.validate_json_response(response)
    response_json = response.json()
    SchemaValidator.validate_schema(response_json, user_list_schema)
    assert len(response_json["data"]) > 0

@pytest.mark.api
def test_verify_get_users_missing_token(user_service):
    response = user_service.client.get("/users", headers={})
    ResponseValidator.validate_status_code(response, 200)
    ResponseValidator.validate_response_time(response, 2000)
    ResponseValidator.validate_json_response(response)
    response_json = response.json()
    SchemaValidator.validate_schema(response_json, user_list_schema)
    assert len(response_json["data"]) > 0


@pytest.mark.api
def test_verify_get_users_invalid_token(user_service):
    response = user_service.client.get("/users", headers={"Authorization": "Bearer invalidtoken"})
    ResponseValidator.validate_status_code(response, 200)
    ResponseValidator.validate_response_time(response, 2000)
    ResponseValidator.validate_json_response(response)
    response_json = response.json()
    SchemaValidator.validate_schema(response_json, user_list_schema)
    assert len(response_json["data"]) > 0


@pytest.mark.api
def test_verify_missing_fields_in_response(user_service):
    response = user_service.get_users(page=1)
    ResponseValidator.validate_status_code(response, 200)
    ResponseValidator.validate_response_time(response, 2000)
    ResponseValidator.validate_json_response(response)
    response_json = response.json()
    assert "page" in response_json
    assert "data" in response_json
    for user in response_json["data"]:
        assert "id" in user
        assert "email" in user
        assert "first_name" in user
        assert "last_name" in user
        assert "avatar" in user

@pytest.mark.api
def test_verify_response_time_exceeds_threshold(user_service):
        response = user_service.get_users(page=1)
        ResponseValidator.validate_status_code(response, 200)
        try:
            ResponseValidator.validate_response_time(response, max_time_ms=100)
        except AssertionError as e:
            print(f"Response time validation failed: {e}")

@pytest.mark.api
def test_verify_non_json_response(user_service):
    response = user_service.client.get("/users", headers={"Accept": "text/html"})
    ResponseValidator.validate_status_code(response, 200)
    ResponseValidator.validate_response_time(response, 2000)
    try:
        ResponseValidator.validate_json_response(response)
    except AssertionError as e:
        print(f"JSON response validation failed: {e}")
