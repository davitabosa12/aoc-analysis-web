from backend.repository.aosp_aoc_report import get_all_reports, search
from backend.model.schema import AoCReportSummarySchema, AoCReportDetailSchema
from flask.blueprints import Blueprint
from flask import request, jsonify
import pandas as pd, json as pd_json
import json

bp_aosp_aoc_report = Blueprint("aosp_aoc_report", __name__)


def parse_project_id(id_: str) -> int:
    if id_.isdigit():
        return int(id_)
    raise ValueError("id is not a valid project_id")


@bp_aosp_aoc_report.route("/")
def get_all_aocs():
    limit = request.args.get("limit", 100)
    if limit > 100:
        limit = 100
    skip = request.args.get("skip", 0)
    result = get_all_reports(limit, skip)
    schema = AoCReportSummarySchema()
    result = schema.dump(result, many=True)
    return jsonify(result)


@bp_aosp_aoc_report.route("/search")
def search_for_aocs():
    project_id, aoc = parse_search_query_params()
    result = search(project_id, aoc)
    schema = AoCReportSummarySchema()
    result = schema.dump(result, many=True)
    return jsonify(result)


def parse_search_query_params():
    project_id = request.args.get("project_id")
    aoc = request.args.get("aoc")
    if project_id:
        project_id = [parse_project_id(id_) for id_ in project_id.split(",") if id_]
    if aoc:
        aoc = [elem for elem in aoc.split(",") if elem]
    return project_id, aoc


@bp_aosp_aoc_report.route("/search/statistics")
def search_aocs_with_statistics():
    project_id, aoc = parse_search_query_params()
    aocs = search(project_id, aoc)
    aocs = AoCReportDetailSchema().dump(aocs, many=True)
    df_aocs = pd.DataFrame.from_records(aocs)
    response = {}
    response["count"] = int(
        df_aocs.count()["id"]
    )  # transforms int64 into python regular 'int' type
    response["class"] = get_statistic_by_class(df_aocs)
    response["aoc"] = get_statistic_by_aoc(df_aocs)
    response["project"] = get_statistic_by_project(df_aocs)
    return jsonify(response)


def get_statistic_by_class(df_aocs) -> dict:
    resp = {}
    for a, b in (
        df_aocs.groupby(by="class")
        .count()
        .sort_values(ascending=False, by="id")["id"]
        .items()
    ):
        resp[a] = b
    return dict(sorted(resp.items(), key=lambda elem: elem[1], reverse=True))


def get_statistic_by_aoc(df_aocs) -> dict:
    resp = {}
    for a, b in (
        df_aocs.groupby(by="aoc")
        .count()
        .sort_values(ascending=False, by="id")["id"]
        .items()
    ):
        resp[a] = b
    return resp


def get_statistic_by_project(df_aocs) -> dict:
    resp = {}
    grouped = df_aocs.groupby(by=lambda elem: df_aocs.loc[elem]["project"]["name"])
    group_names = grouped.groups.keys()
    for group_name in group_names:
        resp[group_name] = {}
        resp[group_name]["count"] = grouped.groups[group_name].size
        resp[group_name]["aoc"] = get_statistic_by_aoc(grouped.get_group(group_name))
        resp[group_name]["class"] = get_statistic_by_class(
            grouped.get_group(group_name)
        )
    return resp
