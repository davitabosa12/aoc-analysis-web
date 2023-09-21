from backend.repository.aoc_report import get_all_reports
from backend.model.schema import AoCReportSummarySchema
from flask.blueprints import Blueprint
from flask import request, jsonify

bp_aoc_report = Blueprint("aoc_report", __name__)

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