from flask import Blueprint, jsonify, request
from flask.views import MethodView
import uuid

from productmng.models import User
auth_bp = Blueprint('auth', __name__)


class AuthAPI(MethodView):
    def post(self):
        req_data = request.get_json()
        user = User.objects(username=req_data['username']).first()
        auth_err_msg = 'Username or password incorrect'
        if user is None:
            return jsonify({'OK': False, 'message': auth_err_msg}), 404
        if user.disabled == True:
            return jsonify({'OK': False, 'message': 'Account is disabled'}), 404
        if user.check_password(req_data['password']) == False:
            return jsonify({'OK': False, 'message': auth_err_msg}), 404

        try:
            user.current_session = str(uuid.uuid4().hex)
            user.save()
        except Exception as error:
            return jsonify({'OK': False, 'message': str(error)}), 404

        return jsonify({'OK': True, 'message': 'authentication ok', 'session': user.current_session, 'user_id': str(user.id)}), 200


auth_view = AuthAPI.as_view('auth')
auth_bp.add_url_rule('/login', view_func=auth_view, methods=['POST', ])
