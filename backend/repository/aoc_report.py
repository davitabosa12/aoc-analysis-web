from backend.db import db_engine
from backend.model.aoc_report import AoCReport
from backend.model.project import Project

from sqlalchemy import select
from sqlalchemy.orm import Session

from typing import List
def get_all_reports(limit: int = 100, skip: int = 0) -> List[AoCReport]:
    with Session(db_engine) as session:
        return session.query(AoCReport).limit(limit).offset(skip).all()

def get_report_by_id(id_: int) -> AoCReport:
    with Session(db_engine) as session:
        return session.query(AoCReport).get(id_)

def get_reports_by_project(project: Project) -> List[AoCReport]:
    stmt = select(AoCReport).where(AoCReport.project_id == project.id)
    with Session(db_engine) as session:
        return session.scalars(stmt)

def get_reports_by_project_id(project_id: int) -> List[AoCReport]:
    stmt = select(AoCReport).where(AoCReport.project_id == project_id)
    with Session(db_engine) as session:
        return session.scalars(stmt)

