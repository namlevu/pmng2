from flask import Blueprint, jsonify, request
from flask.views import MethodView

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
        req_data = request.get_json()
        product = Product(name=req_data['name'],
                          category=req_data['category'],
                          brand=req_data['brand'],
                          sale_price=req_data['sale_price'],
                          history=req_data['history'],
                          note=req_data['note'],
                          sold=req_data['sold']
                          )
        #created_by=current_user # TODO: <--
        costs=req_data['costs']
        for cost in costs:
            cost.save()
            product.costs.append(cost)
        photos=req_data['photos']
        for photo in photos:
            photo.save()
            product.photos.append(photo)

        product.save()

        return jsonify({'OK': True, 'message': 'Hello world Product post', 'req_data':req_data}), 200

    def put(self, product_id):
        product = {}  # TODO: update product
        return jsonify({'OK': True, 'message': 'Hello world Product put', 'product': product}), 200

    def delete(self, product_id):
        product = {}  # TODO: delete product by id
        return jsonify({'OK': True, 'message': 'Hello world Product delete'}), 200


# Register the urls
product_view = ProductAPI.as_view('products')
products_bp.add_url_rule('/products',
                      defaults={'product_id': None},
                      view_func=product_view, methods=['GET', ])
products_bp.add_url_rule('/products', view_func=product_view, methods=['POST', ])
products_bp.add_url_rule('/products/<string:product_id>',
                      view_func=product_view, methods=['GET', 'PUT', 'DELETE'])
