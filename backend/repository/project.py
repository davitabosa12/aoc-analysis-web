from backend.db import db_engine
from backend.model.aoc_report import AoCReport
from backend.model.project import Project

from sqlalchemy import select
from sqlalchemy.orm import Session

from typing import List

def get_all_projects() -> List[Project]:
    with Session(db_engine) as session:
        return session.query(Project).all()

def get_project_by_id(id_: int) -> Project:
    with Session(db_engine) as session:
        return session.query(Project).get(id_)

def get_projects_by_name(name: str) -> List[Project]:
    with Session(db_engine) as session:
        session.query(Project).filter(Project.name.like(name))

def get_projects_by_package_name(package_name: str) -> List[Project]:
    with Session(db_engine) as session:
        session.query(Project).filter(Project.package.like(package_name))