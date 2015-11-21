from flask import jsonify


def error(code, message=""):
    return jsonify({
        "status": "error",
        "code": code,
        "message": message
    })

def ok(message=""):
    return jsonify({
        "status": "OK",
        "message": message
    })
