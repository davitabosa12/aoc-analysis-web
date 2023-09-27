from backend.repository.aoc_report import get_all_reports, search
from backend.model.schema import AoCReportSummarySchema
from flask.blueprints import Blueprint
from flask import request, jsonify

bp_aoc_report = Blueprint("aoc_report", __name__)
def parse_project_id(id_: str) -> int:
    if id_.isdigit():
        return int(id_)
    raise ValueError("id is not a valid project_id")
@bp_aoc_report.route("/")
def get_all_aocs():
    limit = request.args.get("limit", 100)
    if limit > 100:
        limit = 100
    skip = request.args.get("skip", 0)
    result = get_all_reports(limit, skip)
    schema = AoCReportSummarySchema()
    result = schema.dump(result, many=True)
    return jsonify(result)

@bp_aoc_report.route("/search")
def search_for_aocs():
    project_id = request.args.get("project_id")
    aoc = request.args.get("aoc")
    if project_id:
        project_id = [parse_project_id(id_) for id_ in project_id.split(",") if id_]
    if aoc:
        aoc = [elem for elem in aoc.split(",") if elem]
    result = search(project_id, aoc)
    schema = AoCReportSummarySchema()
    result = schema.dump(result, many=True)
    return jsonify(result)