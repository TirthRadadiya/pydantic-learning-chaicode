from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d—%m-%Y %H: %M : %S')} # how you want value to be stored for any data type. here we are storing value of datetime data type in a particular format. We can do for any other data type as well
    )

'''
model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d—%m-%Y %H: %M : %S'), str: lambda v: 'Values'} # how you want value to be stored for any data type. here we are storing value of datetime data type in a particular format. We can do for any other data type as well
    )
-> here whatever variable has string datatype will have 'Values' no matter what you assign

{"id":1,"name":"Values","email":"Values","is_active":false,"createdAt":"15—03-2024 14: 30 : 00","address":{"street":"something","city":"Somewhere","zip_code":"127890"},"tags":["Values","Values"]}

One issue is that if you modify value for any particular datatype all of variable having that datatype will have same customization
'''

user = User(
    id= 1,
    name= "Tirth",
    email= "Tirth@tirth.com" ,
    createdAt = datetime(2024, 3, 15, 14, 30),
    address= Address(
        street = "something",
        city = "Somewhere",
        zip_code = "127890"
    ),
    is_active = False,
    tags = ["premium", "subscriber"],
)

# model_dump() -> coverts to dictionary
dictionary = user.model_dump()
print(dictionary)

print("="*30, "\n")

#.model_dump_json() converts to json
json_data = user.model_dump_json()
print(json_data)