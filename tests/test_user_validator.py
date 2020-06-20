from ..user_validator import *

def test_check_user_by_id():
    check_result = check_user_by_id({'id': 1})
    assert check_result == {'status': True, 'message': 'Data is valid'}

def test_check_user_by_id_fail():
    check_result = check_user_by_id({'i': 1})
    assert check_result == {'status': False,'message': 'Data have not id key'} 

def test_check_user_id_name_data():
    check_result = check_user_id_name_data({'id': 1, 'name': 'Name'})
    assert check_result == {'status': True,'message': 'Data is valid'}


def test_check_user_id_name_data_fail():
    check_result = check_user_id_name_data({'id': 1})
    assert check_result == {'status': False,'message': 'Data is not valid type'}



