from pydantic import BaseModel

'''

Pydantic Data Validation Schemas (Response and Request)

'''

class PlantBase(BaseModel):
    name: str
    status: str
    score: int
    given_comment: int
    
class PlantCreate(PlantBase):
    pass

class CommentBase(BaseModel):
    name: str
    comment: str
    
class CommentCreate(CommentBase):
    pass