# Simple User REST API

### Stack
| Frameworks | 
| ------ | 
| [Flask](https://flask.palletsprojects.com)
| [pytest](https://docs.pytest.org/en/latest/contents.html) | 

User have next fields:
  - id
  - name
  
Data keeps in JSON file (data/data.json)
### Data format
```sh
{'users':[{'id': int, 'name': str]}
```

### Run API
```sh
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python api_server.py
```

### HTTP Requsts URLs
```sh
# get all users 
HTTP GET "https://localhost:5000/"
# curl command
curl "http://127.0.0.1:5000"
# return json format {'users':[{'id': int, 'name': str]}

# get user by id
HTTP GET Header "Content-Type: application/json" "http://127.0.0.1:5000/get_user" Body {"id":1}
# curl command
curl -H "Content-Type: application/json" --request GET --data '{"id": 1}' "http://127.0.0.1:5000/get_user"
# return { "user": {"id": 1, "name": "Test"} }

# add new user
HTTP POST  Header "Content-Type: application/json" "http://127.0.0.1:5000/add_user" Body {"name":"Test"}
# curl commad
curl -H "Content-Type: application/json" --request POST --data '{"name": "Test"}' "http://127.0.0.1:5000/add_user"
# return { "id": 1, "message": "User added successfuly" }

# update user name by id
HTTP PUT Header "Content-Type: application/json" "http://127.0.0.1:5000/update_user" Body {'id': 1, 'name': "New Name"}
# curl commad
curl -H "Content-Type: application/json" --request PUT --data '{"id": 1, "name": "New Name"}' "http://127.0.0.1:5000/update_user"
# return { "message": "User updated successfuly" }

# delete user by id 
HTTP DELETE Header "Content-Type: application/json" "http://127.0.0.1:5000/delete_user" Body {'id': 1}
# curl commad
curl -H "Content-Type: application/json" --request DELETE --data '{"id": 1}' "http://127.0.0.1:5000/delete_user"
# return { "message": "User deleted successfuly", "status": 200 }
```

### Test API
```sh
pytest
# if its all OK
# return
collected 26 items                                                  
tests/test_data_controller.py ........                          [ 30%]
tests/test_user_api.py ..............                           [ 84%]
tests/test_user_validator.py ....                               [100%]
```

