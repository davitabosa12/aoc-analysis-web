from backend.db import db_engine
from backend.model.aoc_report import AoCReport
from backend.model.project import Project

from sqlalchemy import select
from sqlalchemy.orm import Session

from typing import List

def get_aocs() -> List[str]:
    with Session(db_engine) as session:
        # session.query returns a list of tuples
        return [result[0] for result in session.query(AoCReport.aoc).distinct().all()]