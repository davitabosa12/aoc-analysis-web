from backend.model.base import Base
from backend.model.aoc_report import AoCReport, AOSPAoCReport

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from typing import List


class Project(Base):
    __tablename__ = "projects"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(), nullable=False)
    description: Mapped[str] = mapped_column(String(), nullable=True)
    package: Mapped[str] = mapped_column(String(), nullable=False)
    category: Mapped[str] = mapped_column(String(), nullable=False)
    aoc_reports: Mapped[List["AoCReport"]] = relationship(
        back_populates="project", lazy="subquery"
    )


class AOSPProject(Base):
    __tablename__ = "aosp_projects"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(), nullable=False)
    description: Mapped[str] = mapped_column(String(), nullable=True)
    package: Mapped[str] = mapped_column(String(), nullable=False)
    category: Mapped[str] = mapped_column(String(), nullable=False)
    aoc_reports: Mapped[List["AOSPAoCReport"]] = relationship(
        back_populates="project", lazy="subquery"
    )
