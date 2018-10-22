from flask import Blueprint, jsonify, request
from flask.views import MethodView

from productmng.models import User
user_bp = Blueprint('user', __name__)

class UserAPI(MethodView):
    def get(self, user_id):
        success = True
        fail = False
        msg = ""
        if user_id is None:
            users = User.objects.all()
            return jsonify({'OK': success, 'message': msg, 'users': users}), 200
        user = User.objects(id=user_id).first() # TODO: select User by id
        return jsonify({'OK': success, 'message': msg, 'user': user, 'user_id': user_id}), 200

    def post(self):
        req_data = request.get_json()
        user = User(username=req_data['username'], fullname=req_data['fullname'], email=req_data['email'])
        user.set_password(req_data['password_hash'])
        user.disabled = False
        user.save()

        return jsonify({'OK': True, 'message': 'user post', 'req_data':req_data, 'user_id':str(user.id)}), 200

    def put(self, user_id):
        user = {}  # TODO: update User
        return jsonify({'OK': True, 'message': 'user update', 'user': user}), 200

    def delete(self, user_id):
        if user_id is not None:
            user = User.objects(id=user_id).first()
            user.delete()
            return jsonify({'OK': True, 'message': 'user delete'}), 200
        else:
            return jsonify({'OK': False, 'message': 'user delete failed'}), 200

# Register the urls
user_view = UserAPI.as_view('user')
user_bp.add_url_rule('/users',
                      defaults={'user_id': None},
                      view_func=user_view, methods=['GET', ])
user_bp.add_url_rule('/users', view_func=user_view, methods=['POST', ])
user_bp.add_url_rule('/users/<string:user_id>',
                      view_func=user_view, methods=['GET', 'PUT', 'DELETE'])
