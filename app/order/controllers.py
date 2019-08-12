from flask import Blueprint, request, render_template,\
                redirect, url_for
from app import db
from app.order.models import Order
from app.order.helper import convert_to_datetime, format_address 

def insert_order_to_db(order_details):
    """
        Function to insert order to DB
        params:
            order_details : dict
    """
    # converting date to python datetime object
    order_created_at = convert_to_datetime(order_details['created_at'])

    # if phone is not present set to None
    phone_num = None if not order_details['phone'] else order_details['phone']

    # if email is not present set to None 
    email_id = None if not order_details['email'] else order_details['email']

    default_address = order_details['customer']['default_address']
    formatted_address = format_address(default_address)
    try:
        order = Order(  
            id = order_details['order_number'], 
            customer_name = order_details['customer']['first_name'] + ' ' + order_details['last_name'], 
            currency = order_details['customer']['currency'],
            total_price = order_details['total_price'],
            sub_total_price = order_details['sub_total_price'],
            created_at = order_created_at,
            email = email_id, 
            phone_no = phone_num,
            address = formatted_address
        )
        db.session.add(order)
        db.session.commit()
    except Exception:
        return

def get_orders():
    """
        Function to return orders list from Order model.
        return:
            order_list : list of dictionaries.
    """
    try:
        order_list = list()
        orders = Order.query.order_by(Order.created_at).all()
        for order in orders:
            order_list.append(order.__dict__)
        return order_list
    except Exception:
        return None

def get_order(order_id):
    """ 
        Function to get order with given id.
        params:
            order_id : integer
        return:
            order : dict
    """
    try:
        order = Order.query.get(order_id)
        return order.__dict__
    except Exception:
        return None

def update_phone_no(order_id, phone_no):
    """
        Function to update phone number for an order with id 
        order_id.
        params:
            order_id : integer
            phone_no : string
    """
    try:
        order = Order.query.get(order_id)
        order.phone_no = phone_no
        db.session.commit()
        return True
    except Exception:
        return False

def update_email_address(order_id, email):
    """
        Function to update email for an order where
        id is order_id.
        params:
            order_id : integer
            email    : string
    """
    try:
        order = Order.query.get(order_id)
        order.email = email
        db.session.commit()
        return True
    except Exception:
        return False
