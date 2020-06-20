from flask import Flask, jsonify, request, abort
from data_controller import get_all_users, write_new_user, delete_user_by_id, get_user_by_id, update_user_by_id
from user_validator import check_user_data, check_user_by_id, check_user_id_name_data

app = Flask(__name__)

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"status":405, "message": "Method Not Allowed"})

@app.errorhandler(404)
def not_found(e):
    return jsonify({"status":404, "message": "The requested URL was not found on the server"})

@app.errorhandler(500)
def server_error(e):
    return jsonify({"status":500, "message": "Internal Server Error"})

@app.route('/err_500')
def get_server_error():
    abort(500)


@app.route('/')
def get_users():
    data = get_all_users()
    return jsonify(data)

@app.route('/add_user', methods=['POST'])
def add_user():
    """
        Recieve data format {"name": str}

        Returns:
            json:  if success return {'id': int, 'message': 'User added successfuly'}
                   else return {'message': 'Data have not name key'} 
    """
    req = request.get_json()
    check_result = check_user_data(req)
    if check_result['status']:
        new_user_id = write_new_user(req)
        return jsonify(new_user_id)
    else:
        return jsonify({'message':check_result['message']})

@app.route('/delete_user', methods=['DELETE'])
def delete_user():
    """
        Recieve data about user as {'id': int}

        Returns:
            json: if success return {'status': 200, 'message': 'User deleted successfuly'}  
                  else return {'message': User not found please check id}
    """
    req = request.get_json()

    check_result = check_user_by_id(req)
    if check_result['status']:
        result = delete_user_by_id(user_id=req["id"])
        return jsonify({'status': 200, "message": result})
    else:
        return jsonify({'message':check_result['message']})

@app.route('/get_user')
def get_user():
    """
       Recieve request format {'id': int}

       Returns:
            json: if user exists return {'user': {'id': int, 'name': str}}
                  else return {'message': 'User not found please check id'}
                  if request is not valid return {'message': 'Data have not id key'}
    """
    req = request.get_json()
    check_result = check_user_by_id(req)
    if check_result['status']:
        result = get_user_by_id(req['id'])
        if type(result) is dict:
            return jsonify({'user': result})
        else:
            return jsonify({'message':result})
    else:
        return jsonify({'message':check_result['message']})

@app.route('/update_user', methods=['PUT'])
def update_user():
    """
        Recieve request format {'id': int, 'name': str}

        Returns:
            json: if user exists return {'message': 'User updated successfuly'}
                  else return {'message': 'User not found please check id and name keys'}
    """
    req = request.get_json()
    check_result = check_user_id_name_data(req) 
    if check_result['status']:
        update_result = update_user_by_id(req)
        return jsonify({'message': update_result})
    else:
        return jsonify({'message':check_result['message']})

if __name__ == "__main__":
    app.debug = True
    app.run()
