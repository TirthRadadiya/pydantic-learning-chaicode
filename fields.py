from pydantic import BaseModel, Field
from typing import Optional, Dict, List

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]

class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None


'''
Employee Model
- id: number
- name: string and minimum 3 character
- department: optional string with default General value
- salary: float and must be >= 10000
'''

class Employee(BaseModel):
    id: int
    name: str = Field(
        ..., # this means field is required
        min_length=3,
        max_length=50,
        description='Name of an Employee',
        examples=['Tirth Radadiya']
    )
    department: Optional[str] = 'General'
    salary: float = Field(
        ...,
        ge=10000
    )