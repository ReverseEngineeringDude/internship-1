from pydantic import BaseModel,EmailStr,Field
from typing import Dict,Optional

class OrgCreate(BaseModel):
    name: str

class UserCreate(BaseModel):
    name : str
    email : EmailStr 
    password : str = Field(...,min_length=8,max_length=100)
    organization_id : int


class RoleCreate(BaseModel):
    name : str

class AssignUserRole(BaseModel):
    role_id : int
    user_id : int


class PutUser(BaseModel):
    name:str
    email : EmailStr 
    password : str = Field(...,min_length=8,max_length=100)
    organization_id : int

class UpdateParam(BaseModel):
    param: str
    value: str

class MultiUpdate(BaseModel):
    updates: Dict[str, str]

class UpdateUser(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None

