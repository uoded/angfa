from fastapi import APIRouter, Depends, FastAPI, HTTPException
from ...models.models import Project
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/allprojects", response_model=None)
def get_all_projects(db: Session) :
    projects_list = db.query(Project).all()
    try:
        return [projects_list.project_name for project_item in projects_list]
    except Exception :
        return None

@router.get("/projects/{project_id}", response_model= None)
def get_project(project_id: str, db: Session):
    try:
        return db.query(Project).filter(id == project_id).first()
    except Exception :
        return None


@router.put("/projects/{project_id}", response_model=None)
def update_project(project_id: str, updated_data: dict, project: Project, db: Session):
    try:
        project = db.query(Project).filter(id == project_id).first()

        if project:
            for key, value in updated_data.items():
                setattr(project, key, value)
            db.commit()
            db.refresh(project)
            return project
        else:
            raise ValueError(f"Project id {project_id} not found.")
    except Exception:
        return None

@router.post("/projects", response_model=None)
def create_project(new_data: dict, db: Session):
    try:
        new_project = Project(**new_data)
        db.add(new_project)
        db.commit()
        db.refresh(new_project)
        return new_project
    except Exception:
        return None

@router.delete("/projects/{project_id}", response_model=None)
def delete_project(project_id: str, db: Session):
    try:
        project = db.query(Project).filter(id == project_id).first()
        if project:
            db.delete(project)
            db.commit()
            return project
        else:
            raise ValueError(f"Project id {project_id} not found.")
    except Exception:
        return None
    
