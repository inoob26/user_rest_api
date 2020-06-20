import os.path
import json

DB_FILE_PATH = "data/data.json"

def __check_is_file():
    check_result = os.path.isfile(DB_FILE_PATH)
    if check_result != True:
        with open(DB_FILE_PATH, mode='w', encoding='utf-8') as data:
            json.dump({'users':[]},data)
            
def get_all_users():
    """
    Returns:
        users: as json format
    """
    __check_is_file()
    with open(DB_FILE_PATH, mode='r',encoding='utf-8') as data:
        users = json.load(data)
    return users

def write_new_user(user: dict, id=0):
    __check_is_file()
    new_user_name = user['name']
    users = get_all_users()["users"]
    if id != 0 :
        users.append({'id':id, 'name': new_user_name})
        __write_new_user_list_to_file(users)
        return "User added successfuly"

    else:
        id = len(users)
        users.append({'id':id, 'name': new_user_name})
        
        __write_new_user_list_to_file(users)

        return {'id':id,'message': 'User added successfuly'}

def __get_users_for_delete(users: list, id: int):
    for user in users:
        if(user['id'] != id):
            yield user

def __is_user_exist(users: list, id: int):
    match = 0, {}
    for user in users:
        if user['id'] == id:
            match = 1, user
    return match
            

def delete_user_by_id(user_id: int):
    __check_is_file()
    users = get_all_users()["users"]

    if __is_user_exist(users, user_id)[0] == 0:
        return "User not found please check id"
    else:
        new_users = list(__get_users_for_delete(users, user_id))
        __write_new_user_list_to_file(new_users)

        return "User deleted successfuly"

def __write_new_user_list_to_file(users: list):
    with open(DB_FILE_PATH, mode='w', encoding='utf-8') as data:
        json.dump({"users": users}, data)

def get_user_by_id(user_id: int):
    __check_is_file()
    users = get_all_users()["users"]
    check_result = __is_user_exist(users, user_id)
    if check_result[0] == 0:
        return "User not found please check id"
    else:
        return check_result[1]

def __update_user_by_id_name(users: list, user_id: int, new_user_name: str):
    for user in users:
        if user['id'] == user_id:
            user['name'] = new_user_name
    __write_new_user_list_to_file(users)

def update_user_by_id(user: dict):
    __check_is_file()
    users = get_all_users()["users"]
    check_result = __is_user_exist(users, user['id'])
    if check_result[0] == 0:
        return "User not found please check id and name keys"
    else:
        __update_user_by_id_name(users, user['id'], new_user_name=user['name'])
        return "User updated successfuly"
