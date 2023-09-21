from flask import jsonify, Response

from http import HTTPStatus


def make_error_response(
    status: str | int | HTTPStatus = HTTPStatus.BAD_REQUEST,
    message: str = "Client Error",
    extra_data: dict = None,
) -> Response:
    error_message = {"message": message}
    if extra_data:
        error_message.update(extra_data)
    error_message = jsonify(error_message)
    error_message.status = status
    return error_message
