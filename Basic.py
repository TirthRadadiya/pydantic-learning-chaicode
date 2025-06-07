from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {
    "id": 101,
    'name': 'Stein',
    'is_active': True
}

user = User(**input_data)

print(user) #id=101 name='Stein' is_active=True

# input_data = {
#     "id": 101,
#     'name': 'Stein',
#     'isActive': True
# }

user = User(**input_data)
# print(user) 
'''
is_active
  Field required [type=missing, input_value={'id': 101, 'name': 'Stein', 'isActive': True}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.11/v/missing
'''

input_data = {
    "id": 101,
    'name': 'Stein',
    'is_active': 'True'
}

user = User(**input_data)

# print(user) #id=101 name='Stein' is_active=True

# here pydantic will typecast automatically. It can typecase untill certain limit. 'is_active': 'correct' -> this will result in error

input_data = {
    "id": '101',
    'name': 'Stein',
    'is_active': True
}

user = User(**input_data)

print(user) #id=101 name='Stein' is_active=True
# here also pydantic type case but it will be for certain limit


class UserWithDefaultName(BaseModel):
    id: int
    name: str = 'User'
    is_active: bool

input_data = {
    "id": '101',
    'is_active': True
}

user = UserWithDefaultName(**input_data)

print(user) #id=101 name='User' is_active=True
# this is how you can give default value