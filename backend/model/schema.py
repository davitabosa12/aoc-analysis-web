from marshmallow import Schema, fields

class AoCReportSummarySchema(Schema):
    id = fields.Integer()
    line = fields.Integer()
    snippet = fields.String()
    class_ = fields.String(data_key="class")
    aoc = fields.String()
    path = fields.String()

class ProjectSummarySchema(Schema):
    id = fields.Integer()
    name  = fields.String()
    description = fields.String()
    package = fields.String()
    category = fields.String()

class AoCReportDetailSchema(Schema):
    id = fields.Integer()
    project_id = fields.Integer()
    project = fields.Nested(ProjectSummarySchema())
    line = fields.Integer()
    snippet = fields.String()
    class_ = fields.String(attribute="class")
    aoc = fields.String()
    path = fields.String()

class ProjectDetailSchema(Schema):
    id = fields.Integer()
    name  = fields.String()
    description = fields.String()
    package = fields.String()
    category = fields.String()
    aoc_reports = fields.List(fields.Nested(AoCReportSummarySchema()))