from backend.repository.aosp_project import (
    get_all_aosp_projects,
    get_aosp_project_by_id,
    get_aosp_projects_by_name,
    get_aosp_projects_by_package_name,
)
from backend.model.schema import ProjectSummarySchema, ProjectDetailSchema
from backend.controller.error import make_error_response
from flask.blueprints import Blueprint
from flask import request, jsonify

bp_aosp_projects = Blueprint("aosp_project", __name__)


@bp_aosp_projects.route("/")
def all_projects():
    result = get_all_aosp_projects()
    schema = ProjectSummarySchema()
    result = schema.dump(result, many=True)
    return jsonify(result)


@bp_aosp_projects.route("/<int:project_id>")
def project_by_id(project_id):
    result = get_aosp_project_by_id(project_id)
    schema = ProjectDetailSchema()
    result = schema.dump(result)
    return jsonify(result)


@bp_aosp_projects.route("/search")
def search_project():
    name_query = request.args.get("name")
    package_query = request.args.get("package")
    if name_query:
        result = get_aosp_projects_by_name(name_query)
    elif package_query:
        result = get_aosp_projects_by_package_name(package_query)
    else:
        return make_error_response(message="Should pass 'name' or 'package'")
    schema = ProjectDetailSchema()
    result = schema.dump(result, many=True)
    return jsonify(result)
