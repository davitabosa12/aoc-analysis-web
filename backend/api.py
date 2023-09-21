from flask.blueprints import Blueprint
from backend.controller.aoc_report import bp_aoc_report
from backend.controller.project import bp_projects
from backend.controller.aoc import bp_aoc
bp_api = Blueprint("api", __name__)
bp_api.register_blueprint(bp_aoc_report, url_prefix="/aoc-reports")
bp_api.register_blueprint(bp_projects, url_prefix="/project")
bp_api.register_blueprint(bp_aoc, url_prefix="/aoc")
