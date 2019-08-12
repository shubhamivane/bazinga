from flask import Blueprint, request, render_template,\
                redirect, url_for, jsonify
from app.order.controllers import get_orders, get_order,\
                update_email_address, update_phone_no, insert_order_to_db
from app.order.helper import verify_webhook
import json

order = Blueprint('order', __name__, url_prefix='')

@order.route('/', methods=['GET'])
def index():
    """
        Index view display all orders.
    """
    orders = get_orders()
    return render_template('order/index.html', orders = orders)

@order.route('/order/<int:order_id>/', methods=['GET'])
def _order(order_id):
    """
        Display details related to an order.
        params:
            id : order id
    """
    order = get_order(order_id)
    response = {'email': None, 'phone_no': None, 'order_id': order_id}
    if order:
        response['phone_no'] = order.get('phone_no')
        response['email'] = order.get('email')
    return render_template('order/order.html', response=response)

@order.route('/update/phone', methods=['POST'])
def update_phone():
    order_id = request.args.get('order_id')
    phone_no = request.args.get('phone_no')
    if update_phone_no(order_id, phone_no):
        return 'Successfully updated.'
    else:
        return 'Couldn\'t update try again later.'

@order.route('/update/email', methods=['POST'])
def update_email():
    order_id = request.args.get('order_id')
    email = request.args.get('email')
    if update_email_address(order_id, email):
        return 'Successfully updated.'
    else:
        return 'Couldn\'t update try again later.'

@order.route('/shopify/order-creation/', methods=['POST'])
def webhook():
    """
        Webhook endpoint triggered by Shopify when
        any order is created on the Shop.
    """
    # hmac sent by shopify
    shopify_hmac = request.headers.get('X-Shopify-Hmac-Sha256')

    # payload in bytes
    shopify_payload = request.get_data()
    if verify_webhook(shopify_payload, shopify_hmac):
        data = json.loads(shopify_payload)
        insert_order_to_db(data)
        return jsonify({'message': 'webhook received', 'status': 'OK'})
    else:
        abort(401)