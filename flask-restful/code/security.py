from users import User

users = [User(1, 'shubham', 's1234'), User(2, 'ashish', 'a1234')]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and user.password == password:
        return user
    else:
        return {'message': 'Not valid username or password!'}


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)

