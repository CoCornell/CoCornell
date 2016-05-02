from flask import g, redirect, url_for, jsonify
from flask.ext.login import login_required

from mysite import app
from mysite.models.list import List


@app.route("/list/<int:list_id>/", methods=['DELETE'])
@login_required
def delete_list(list_id):
    """
    Deletes a list.
    """
    if not List.has_access_to(g.user.netid, list_id):
        return redirect(url_for('board'))
    List.delete_list_by_id(list_id)
    return jsonify({"deleted": True})
