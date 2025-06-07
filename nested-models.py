from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address # here refrenced another class

class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List['Comment']] = None # here refrence it's own class. This is called forward referencing

Comment.model_rebuild() # this needs to be done to proper use forward refrencing

address = Address(
    street="Somwhere in Amedabad",
    city='Ahmedabad',
    postal_code='234567'
)

user =  User(
    id= 3,
    name='Tirth',
    address=address
)

comment = Comment(
    id= 2,
    content='Hey there!!!',
    replies=[
        Comment(id=2, content='How is it going'),
        Comment(id=3, content='Good till now')
    ]
)

# TODO: Create Course model
# Each Course has modules
# Each Module has lessons


class Lesson(BaseModel):
    id: int
    name: str
    runtime: Optional[str] = '00:00'

class Modules(BaseModel):
    id: int
    name: str
    lessons: List[Lesson]

class Course(BaseModel):
    id: int
    name: str
    instructor: str
    modules:  List[Modules]

course = Course(
    id= 3,
    name= 'Generative AI',
    instructor='Tony Stark',
    modules=[
        Modules(id=20, name='Pre-requisites', lessons=[
            Lesson(id=30, name='Python'),
            Lesson(id=90, name='OOPS in Python and Advance Python', runtime='180:00')
        ]),
        Modules(
            id=50,
            name='Backend',
            lessons=[
                Lesson(id=91, name='Overview of Backend'),
                Lesson(id=32, name='FastAPI')
            ]
        )
    ]
)

print(course.modules)

