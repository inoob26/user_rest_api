import pytest
from ..data_controller import *

@pytest.fixture
def add_user_for_test():
    write_new_user({'name': 'Test Name'})
    yield
    delete_user_by_id(0)


def test_write_new_user():
    new_user_id = write_new_user({'name': 'Test Name'})
    assert new_user_id == {'id': 0, 'message': 'User added successfuly'} 
    #teardown
    delete_user_by_id(0)

def test_delete_user_by_id(add_user_for_test):
    delete_result = delete_user_by_id(0)
    assert delete_result == "User deleted successfuly"

def test_delete_user_by_id_fail():
    delete_result = delete_user_by_id(0)
    assert delete_result == "User not found please check id"
   
def test_get_all_users(add_user_for_test):
    get_users_result = get_all_users()
    assert get_users_result == {"users": [{"id":0,"name": "Test Name"}]}

def test_get_user_by_id(add_user_for_test):
    get_user_result = get_user_by_id(0)
    assert get_user_result == {"id":0, "name": "Test Name"}
    
def test_get_user_by_id_fail():
    get_user_result = get_user_by_id(1000)
    assert get_user_result == "User not found please check id"   

def test_update_user_by_id(add_user_for_test):
    update_user_result = update_user_by_id({"id":0, "name": "New Test Name"})
    assert update_user_result == "User updated successfuly"

def test_update_user_by_id_fail(add_user_for_test):
    update_user_result = update_user_by_id({"id":1000, "name": "New Test Name"})
    assert update_user_result == "User not found please check id and name keys"

