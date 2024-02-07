from pydantic import BaseModel


class Project(Base):

    id = int
    name = str
    description = str
    
    class Config:
        orm_mode = True
