from flask import jsonify
from mysite.api.const import Error


def error(code, status_code=None):
    ret = jsonify({
        "status": "error",
        "code": code,
        "message": Error.error_message(code)
    })
    if status_code:
        ret.status_code = status_code
    return ret


def ok(data):
    data['status'] = 'OK'
    return jsonify(data)
