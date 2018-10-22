from flask import Blueprint, jsonify, request
from flask.views import MethodView
import datetime

from productmng.models import Photo, User, Cost, Product
products_bp = Blueprint('products', __name__)


class ProductAPI(MethodView):
    def get(self, product_id):
        success = True
        fail = False
        msg = ""
        if product_id is None:
            products = Product.objects.all()
            return jsonify({'OK': success, 'message': msg, 'products': products}), 200
        product = Product.objects(id=product_id).first() # TODO: select product by id
        return jsonify({'OK': success, 'message': msg, 'product': product, 'product_id': product_id}), 200

    def post(self):
        try:
            req_data = request.get_json()
            current_user = User.objects(id=request.headers.get('user_id')).first()
            import ast
            product = Product(name=req_data['name'],
                              category=req_data['category'],
                              brand=req_data['brand'],
                              sale_price=req_data['sale_price'],
                              history=req_data['history'],
                              note=req_data['note'],
                              sold=ast.literal_eval(req_data['sold'])
                              )

            costs=req_data['costs']
            for cost_item in costs:
                cost = Cost(amount=cost_item['amount'], reason=cost_item['reason'], created_by=current_user.id)
                product.costs.append(cost)

            photos=req_data['photos']
            for photo_item in photos:
                photo = Photo(url=photo_item['url'])
                product.photos.append(photo)

            product.created_by = current_user.id
            product.save()
        except Exception as e:
            return jsonify({'OK': False, 'message': str(e)}), 401

        return jsonify({'OK': True, 'message': 'Product created successful', 'product':product}), 200

    def put(self, product_id):
        try:
            req_data = request.get_json()
            current_user = User.objects(id=request.headers.get('user_id')).first()
            product = Product.objects(id=product_id).first()

            product.update(name=req_data['name'],
                              category=req_data['category'],
                              brand=req_data['brand'],
                              sale_price=req_data['sale_price'],
                              history=req_data['history'],
                              note=req_data['note'],
                              sold=bool(req_data['sold']),
                              costs=req_data['costs'],
                              photos=req_data['costs'],
                              updated_by=current_user.id,
                              updated_at=datetime.datetime.now
                              )

        except Exception as e:
            print("Error----------------------------------");
            return jsonify({'OK': False, 'message': str(e)}), 401
        return jsonify({'OK': True, 'message': 'Product updated successful', 'product': product}), 200

    def delete(self, product_id):
        product = Product.objects(id=product_id).first()
        product.delete()

        return jsonify({'OK': True, 'message': 'Product deleted successful'}), 200


# Register the urls
product_view = ProductAPI.as_view('products')
products_bp.add_url_rule('/products',
                      defaults={'product_id': None},
                      view_func=product_view, methods=['GET', ])
products_bp.add_url_rule('/products', view_func=product_view, methods=['POST', ])
products_bp.add_url_rule('/products/<string:product_id>',
                      view_func=product_view, methods=['GET', 'PUT', 'DELETE'])
