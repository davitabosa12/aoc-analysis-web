from backend.db import aosp_db_engine
from backend.model.aoc_report import AOSPAoCReport
from backend.model.project import AOSPProject

from sqlalchemy import select
from sqlalchemy.orm import Session

from typing import List


def get_all_aosp_projects() -> List[AOSPProject]:
    with Session(aosp_db_engine) as session:
        return session.query(AOSPProject).all()


def get_aosp_project_by_id(id_: int) -> AOSPProject:
    with Session(aosp_db_engine) as session:
        return session.query(AOSPProject).get(id_)


def get_aosp_projects_by_name(name: str) -> List[AOSPProject]:
    with Session(aosp_db_engine) as session:
        session.query(AOSPProject).filter(AOSPProject.name.like(name))


def get_aosp_projects_by_package_name(package_name: str) -> List[AOSPProject]:
    with Session(aosp_db_engine) as session:
        session.query(AOSPProject).filter(AOSPProject.package.like(package_name))
