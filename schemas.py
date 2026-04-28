from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, EmailStr


class UserBase(BaseModel):
    username: str = Field(min_length=1, max_length=50)
    email: str = Field(max_length=150)

class UserCreate(UserBase):
    pass

class UserUpdate(BaseModel):
    username: str | None = Field(default=None, min_length=1, max_length=50)
    email: EmailStr | None = Field(default=None, max_length=150)
    image_file: str | None = Field(default=None,min_length=1, max_length=200)

class UserResponse(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    image_file: str | None
    image_path: str

class PostBase(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    content: str = Field(min_length=1)

# Create Post schema
class PostCreate(PostBase):
    user_id: int  #Temporary

class PostUpdate(BaseModel):
    title: str = Field(default=None, max_length=100)
    content: str = Field(default=None, min_length=1)

# Create Post response
class PostResponse(PostBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    date_posted: datetime
    author: UserResponse