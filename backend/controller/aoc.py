from backend.repository.aoc import get_aocs
from backend.model.schema import AoCReportSummarySchema
from flask.blueprints import Blueprint
from flask import request, jsonify

bp_aoc = Blueprint("aoc", __name__)

@bp_aoc.route("/")
def get_all_aocs():
    aocs = get_aocs()
    return jsonify(aocs)
