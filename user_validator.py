import json

def check_user_data(user: dict):
    result = __get_status_and_check_message(user, "name")
    return result

def check_user_by_id(user: dict):
    result = __get_status_and_check_message(user, "id")
    return result

def check_user_id_name_data(user: dict):
    result_id = __get_status_and_check_message(user, "id")
    result_name = __get_status_and_check_message(user, "name")

    if result_id['status'] and result_name['status'] == True:
        return {'status': True,'message': 'Data is valid'}
    else:
        return {'status': False,'message': 'Data is not valid type'}


def __get_status_and_check_message(user: dict, key: str):
    if type(user) is dict:
        if key in user:
            return {'status': True,'message': 'Data is valid'}
        else:
            return {'status': False,'message': f'Data have not {key} key'}
    else:
        return {'status': False,'message': 'Data is not valid type'}
