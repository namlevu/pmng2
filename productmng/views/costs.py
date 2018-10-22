from flask import Blueprint, jsonify, request
from flask.views import MethodView

from productmng.models import Cost
costs_bp = Blueprint('costs', __name__)

class CostAPI(MethodView):
    def get(self):
        return jsonify({'OK': True, 'message': 'Cost get'}), 200

cost_view = ProductAPI.as_view('costs')
costs_bp.add_url_rule('/costs',
                      defaults={'cost_id': None},
                      view_func=cost_view, methods=['GET', ])
costs_bp.add_url_rule('/costs', view_func=cost_view, methods=['POST', ])
costs_bp.add_url_rule('/costs/<string:cost_id>',
                      view_func=cost_view, methods=['GET', 'PUT', 'DELETE'])
