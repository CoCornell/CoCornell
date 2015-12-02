from flask import request, g

from mysite.models.list import List
from mysite.api import api
from mysite.api.const import Error
from mysite.api.utils import ok, error
from mysite.api.token import auth


@api.route("/list/<int:list_id>/", methods=['GET', 'DELETE'])
@auth.login_required
def delete_list(list_id):
    if not List.has_access_to(g.user.netid, list_id):
        return error(Error.NO_ACCESS_TO_LIST)

    if request.method == 'DELETE':
        List.delete_list_by_id(list_id)
        return ok({"deleted": True})
