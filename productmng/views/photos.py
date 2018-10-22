from flask import Blueprint, jsonify, request
from flask.views import MethodView

from productmng.models import Cost
photos_bp = Blueprint('photos', __name__)

class PhotoAPI(MethodView):
    def get(self):
        return jsonify({'OK': True, 'message': 'Photo get'}), 200
