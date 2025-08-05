#Generic types hints List
import datetime
from pydantic import BaseModel
from typing import Optional, Annotated


def process_items(items : list[str]): # [str] type parameters in java is List<String>
    for item in items:
        print(item)

#Generic types hints tuples and set
def process_items(items_t : tuple[int, int, str], items_s: set[bytes]):
    return items_t, items_s

#Generic types hints Dict
def process_items(prices: dict[str, float]):
    for item_name, item_price in prices.items():
        print(item_name)
        print(item_price)

#Generic types hints Union. A variable can be any of several types, for example, an int or a str.
def process_items(item: int | str):
    print(item)

#Generic types hints Possibly | Union
#Optional[Something] is actually a shortcut for Union[Something, None], they are equivalent.
def say_hi(name: Optional[str] = None):
    if name is not None:
        print(f"Hey {name}!")
    else:
        print("Hello World")

def say_hi(name: str | None = None):
    if name is not None:
        print(f"Hello {name}")
    else:
        print("Hello World")

# *****  Classes as types ******
class Person:
    def __init__(self, name: str):
        self.name = name

def get_person_name(one_person: Person):
    return one_person.name

# ***** Pydantic models ******
class User(BaseModel):
    id: int
    name: str = "John Doe"
    signup_ts: datetime | None = None
    friends: list[int] = []

external_data = {
    "id": "123",
    "signup_ts": "2021-09-22 12:22",
    "friends": [1, "2", b"3"]
}

user = User(**external_data)
print(user)
print(user.id)

# ******* Metadata Annotations ******
# Annotated to provide FastAPI with additional metadata about how you want your application to behave.
# the first type parameter you pass to Annotated is the actual type. The rest, is just metadata for other tools.
def say_hello(name: Annotated[str, "This is just metadata"]) -> str:
    return f"Hello {name}"