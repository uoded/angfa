from sqlalchemy import Column, Integer, String
from app.api.databaseconnexion.database import Base

class Project(Base):
    __tablename__ = "CRUD"

    id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String, index=True)
    description = Column(String)
