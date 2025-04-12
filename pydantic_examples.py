from pydantic import BaseModel, ValidationError, EmailStr

# Define a simple model
class User(BaseModel):
    id: int
    name: str
    email: str
    age: int | None = None # Optional field with the default set as None

# Valid data
user_data = {"id": 1, "name": "Alice", "email": "alice@example.com", "age": 25}
user = User(**user_data)
print(user)  # id=1 name='Alice' email='alice@example.com' age=25
print(user.model_dump())  # {'id': 1, 'name': 'Alice', 'email': 'alice@example.com', 'age': 25}

# Invalid data (will raise an error)
# try:
#     invalid_user = User(id="not_an_int", name="Bob", email="bob@example.com")
# except ValidationError as e:
#     print(e)

# Define a nested model
class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class UserWithAddress(BaseModel):
    id: int
    name: str
    email: EmailStr
    addresses: list[Address]

# valid data with nested structure
user_data = {
    "id" : 2,
    "name" : "Bethany",
    "email" : "bethany@example.com",
    "addresses": [
        {"street": "123 Main St", "city": "New York", "zip_code": "10001"},
        {"street": "456 Oak Ave", "city": "Los Angeles", "zip_code": "90001"},
    ],  
}
user = UserWithAddress.model_validate(user_data)
print(user.model_dump())