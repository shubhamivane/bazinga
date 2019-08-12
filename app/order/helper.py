from datetime import datetime
import base64
import hashlib
import hmac
from app import app


def convert_to_datetime(date):
    """
        Function to convert '2019-08-11T04:28:32-04:00' format to 
        python datetime object.
        params:
            date : string ('2019-08-11T04:28:32-04:00')
        return:
            date_object : python datetime object
    """
    year, month, tmp, _ = date.split('-')
    day, tmp = tmp.split('T')
    hours, minutes, seconds = tmp.split(':')
    return datetime(int(year), int(month), int(day), int(hours), int(minutes), int(seconds))

def format_address(address):
    """
        Function to convert address dictionary to fomatted
        params:
            address : dict
        return:
            formatted_address : string
    """
    formatted_address = address['address1'] + ' ' + address['address2'] +\
        ', ' + address['city'] +' ' + address['province'] + ' ' + address['zip'] +\
        ' ' + address['country_name']
    return formatted_address

def verify_webhook(data, hmac_header):
    """ 
        Function to verify webhook by comparing computed hmac with hmac sent by shopify 
        params:
            data : Bytes or Bytes array
            hmac_header : string

        return:
            True  : If computed hmac and shopify hmac is same.
            False : If computed hmac and shopify hmac is different.
    """
    digest = hmac.new(app.config['SHOPIFY_KEY'], data, hashlib.sha256).digest()
    computed_hmac = base64.b64encode(digest)
    return hmac.compare_digest(computed_hmac, hmac_header.encode('utf-8'))