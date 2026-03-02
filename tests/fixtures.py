import pytest
from fastapi.encoders import jsonable_encoder
########auth############
@pytest.fixture
def mock_header():
    return {
        "Authorization": "test_token"
        
    }

#########input data##############
@pytest.fixture
def valid_create_data():
    return {
        "title": "valid",
        "content": "valid content",
    }


@pytest.fixture
def existing_create_data():
    return {
        "title": "existing_title",
        "content": "valid content",
    }

@pytest.fixture
def valid_update_data():
    return {
        "title": "valid",
        "content": "valid content",
    }

########Responses#################
@pytest.fixture
def valid_create_response_data():
    return jsonable_encoder({
        "title": "valid",
        "content": "valid content",
        "author": "test",
        "id": 1
    })

@pytest.fixture
def post_already_exists_response():
    return jsonable_encoder({
        "detail": "Post already exists"
    })


@pytest.fixture
def valid_post_delete_response():
    return jsonable_encoder({
        "success":"Post deleted!"
    })

@pytest.fixture
def post_not_found_response():
    return jsonable_encoder({
        "detail":"Post not found!"
    })

@pytest.fixture
def forbidden_response():
    return jsonable_encoder({
        "detail":"You are not the author"
    })

@pytest.fixture
def valid_update_response_data():
    return jsonable_encoder({
        "title": "valid",
        "content": "valid content",
        "author": "test",
        "id": 1
    })

@pytest.fixture
def valid_get_response_data():
    return jsonable_encoder([{
        "title": "valid",
        "content": "valid content",
        "author": "test",
        "id": 1
    }])




