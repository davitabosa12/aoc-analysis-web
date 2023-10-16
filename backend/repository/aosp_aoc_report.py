from backend.db import aosp_db_engine
from backend.model.aoc_report import AOSPAoCReport
from backend.model.project import AOSPProject

from sqlalchemy import select, and_, or_, false, true
from sqlalchemy.orm import Session

from typing import List


def get_all_reports(limit: int = 100, skip: int = 0) -> List[AOSPAoCReport]:
    with Session(aosp_db_engine) as session:
        return session.query(AOSPAoCReport).limit(limit).offset(skip).all()


def get_report_by_id(id_: int) -> AOSPAoCReport:
    with Session(aosp_db_engine) as session:
        return session.query(AOSPAoCReport).get(id_)


def get_reports_by_project(project: AOSPProject) -> List[AOSPAoCReport]:
    stmt = select(AOSPAoCReport).where(AOSPAoCReport.project_id == project.id)
    with Session(aosp_db_engine) as session:
        return session.scalars(stmt)


def get_reports_by_project_id(project_id: int) -> List[AOSPAoCReport]:
    stmt = select(AOSPAoCReport).where(AOSPAoCReport.project_id == project_id)
    with Session(aosp_db_engine) as session:
        return session.scalars(stmt)


def search(project_id: int | List[int] = None, aoc: str | List[str] = None):
    and_clauses = []
    if project_id is None:
        project_id = []
    list_project_ids = project_id if isinstance(project_id, list) else [project_id]
    if list_project_ids:
        and_clauses.append(
            or_(
                false,
                *[AOSPAoCReport.project_id == proj_id for proj_id in list_project_ids]
            )
        )
    if aoc is None:
        aoc = []
    list_aocs = aoc if isinstance(aoc, list) else [aoc]
    if aoc:
        and_clauses.append(
            or_(false, *[AOSPAoCReport.aoc.like(aoc_elem) for aoc_elem in list_aocs])
        )
    stmt = select(AOSPAoCReport).where(and_(true, *and_clauses))
    with Session(aosp_db_engine) as session:
        reports = []
        for scalar in session.scalars(stmt):
            reports.append(scalar)
        return reports
