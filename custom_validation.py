from pydantic import BaseModel, field_validator, model_validator, computed_field

class User(BaseModel):
    '''
    field validator runs before - need to check more in this
    To validate single value use field validator
    '''
    username: str

    @field_validator('username') # runs before pydantic
    def username_length(cls, value):
        if len(value):
            raise ValueError("Username must be atleast 4 characters")
        return value
    
class SignUpData(BaseModel):
    '''
    here we can provide many modes. after mode means this will run after all custom validator and pydantic has completed it's job
    when you want to validate multiple values from single class use mode validator
    '''
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def match_password(cls, values):
        if values.passwords != values.confirm_password:
            raise ValueError("Password Do not Match")
        return values
    

class Product(BaseModel):
    '''
    computed_field are used to created value which can be computed based on other fields
    '''
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
    

'''
Create Booking model
Fields:
- user_id: int
- room_id: int
- nights: int (must be >=1)
- rate_per_night: float I
Also, add computed field: total_amount = nights *
rate_per_night
'''

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int
    # nights: int = Field(..., ge=1)
    rate_per_night: int = 1000000

    @field_validator('nights')
    def nights_checking(cls, value):
        if value < 1:
            raise ValueError("You should stay atleast 1 night. It's fantastic experience")
        return value
    
    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night