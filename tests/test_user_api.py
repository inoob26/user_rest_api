import pytest
from ..api_server_for_pytest import app
from collections import OrderedDict
from ..data_controller import write_new_user, delete_user_by_id


@pytest.fixture
def add_user_for_test():
    
    write_new_user({"name":"Test_Name"}, id=999)
    yield
    
    #teardown
    delete_user_by_id(999)

def test_get_users(add_user_for_test):
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.is_json == True
    user = response.get_json()['users'][-1]
    assert user == {"id": 999, "name": 'Test_Name'}
    

def test_get_users_fail():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.is_json == True
    user = response.get_json()['users']
    assert user != {"id": 999, "name": 'Test_Name'}

def test_create_user():
    response = app.test_client().post('/add_user', json={'name': 'John'})
    
    assert response.status_code == 200
    assert response.is_json == True
    response_json = response.get_json()
    assert response_json['message'] == "User added successfuly"
    
    # teardown
    delete_user_by_id(response_json['id'])


def test_create_user_fail():
    response = app.test_client().post('/add_user', json={'na': 'John'})
    
    assert response.status_code == 200
    assert response.is_json == True
    response_json = response.get_json()
    assert response_json['message'] == "Data have not name key"

def test_delete_user_by_id(add_user_for_test):
    response = app.test_client().delete('/delete_user/', json={'id': 999})

    assert response.status_code == 200
    assert response.is_json == True
    response_json = response.get_json()
    assert response_json['message'] == "User deleted successfuly"


def test_delete_user_by_id_fail():
    response = app.test_client().delete('/delete_user/', json={'id': 999})

    assert response.status_code == 200
    assert response.is_json == True
    response_json = response.get_json()
    assert response_json['message'] == "User not found please check id"

def test_get_user_by_id(add_user_for_test):
    response = app.test_client().get('/get_user', json={'id': 999})

    assert response.status_code == 200
    assert response.is_json == True
    response_json = response.get_json()
    assert response_json['user'] == {'id':999, "name":"Test_Name"}

def test_get_user_by_id_fail():

    response = app.test_client().get('/get_user', json={'id': 999})

    assert response.status_code == 200
    assert response.is_json == True
    response_json = response.get_json()
    assert response_json['message'] == "User not found please check id"

def test_get_user_by_id_request_type_fail():
    response = app.test_client().get('/get_user', json={'d': 999})

    assert response.status_code == 200
    assert response.is_json == True
    response_json = response.get_json()
    assert response_json['message'] == "Data have not id key"

def test_update_user_by_id(add_user_for_test):
    response = app.test_client().put('/update_user', json={'id': 999, 'name': 'Another Name'})
    assert response.status_code == 200
    assert response.is_json == True
    response_json = response.get_json()
    assert response_json['message'] == "User updated successfuly"


def test_update_user_by_id_fail():
    response = app.test_client().put('/update_user', json={'id': 999, 'name': 'Another Name'})
    assert response.status_code == 200
    assert response.is_json == True
    response_json = response.get_json()
    assert response_json['message'] == "User not found please check id and name keys"

def test_error_method_not_allowed():
    response = app.test_client().get('/update_user', json={'id': 999, 'name': 'Another Name'})
    assert response.status_code == 200
    assert response.is_json == True
    response_json = response.get_json()
    assert response_json['message'] == "Method Not Allowed"


def test_error_not_found():
    response = app.test_client().get('/some_uri')
    assert response.status_code == 200
    assert response.is_json == True
    response_json = response.get_json()
    assert response_json['message'] == "The requested URL was not found on the server" 

def test_error_server_error():
    response = app.test_client().get('/err_500')
    assert response.status_code == 200
    assert response.is_json == True
    response_json = response.get_json()
    assert response_json['message'] == "Internal Server Error"


