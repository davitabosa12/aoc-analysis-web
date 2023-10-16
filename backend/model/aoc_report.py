from backend.model.base import Base

from marshmallow import Schema, fields

from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class AoCReport(Base):
    __tablename__ = "aoc_reports"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"))
    project: Mapped["Project"] = relationship(
        back_populates="aoc_reports", lazy="subquery"
    )
    line: Mapped[int] = mapped_column(Integer())
    snippet: Mapped[str] = mapped_column(String(), nullable=False)
    class_: Mapped[str] = mapped_column(String(), nullable=False, name="class")
    aoc: Mapped[str] = mapped_column(String(), nullable=False)
    path: Mapped[str] = mapped_column(String(), nullable=True)


class AOSPAoCReport(Base):
    __tablename__ = "aosp_aoc_reports"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("aosp_projects.id"))
    project: Mapped["AOSPProject"] = relationship(
        back_populates="aoc_reports", lazy="subquery"
    )
    line: Mapped[int] = mapped_column(Integer())
    snippet: Mapped[str] = mapped_column(String(), nullable=False)
    class_: Mapped[str] = mapped_column(String(), nullable=False, name="class")
    aoc: Mapped[str] = mapped_column(String(), nullable=False)
    path: Mapped[str] = mapped_column(String(), nullable=True)
    loc: Mapped[int] = mapped_column(Integer(), nullable=True)
    commit: Mapped[str] = mapped_column(String(), nullable=False)
