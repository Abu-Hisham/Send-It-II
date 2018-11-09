from flask import Blueprint, request, jsonify
from app.api.V1.models import Parcel,User
bp = Blueprint('app', __name__, url_prefix='/api/v1/')
@bp.route('/')
@bp.route('/index')
def index():
    return "Hello, World!"


@bp.route('/users',methods=['POST'])
def create_user():
    data = request.get_json()
    username = data['username']
    email = data['email']
    phone = data['phone']
    password = data['password']

    user = User(username, email, phone, password)
    if user in User.user_list:
        message = {'username': user.username,
                   'status': 'User Exists'}
        response = jsonify(message)
        response.status_code = 300
        return response
    else:
        User.user_list.append(user)
        message = {'username': user.username,
                   'status': 'User created successfully'
                   }
        response = jsonify(message)
        response.status_code = 201
        return response


@bp.route('/parcels')
def get_parcels():
    # data = request.get_json()
    # username = data['username']
    # email = data['email']
    # password = data['password']
    # user_id = data['user_id']
    # user = User(user_id, username, email, password)
    # if user in User.user_list:
    #     message = {'username': user.username,
    #                'status': 'User Exists'}
    #     return jsonify(message)
    # else:
    #     User.user_list.append(user)
    #     message = {'username': user.username,
    #                'status': 'User created successfully'
    #                }
    #     return jsonify(message)
    pass


@bp.route('/parcels', methods=['POST'])
def create_parcel_delivery_order():
    data = request.get_json()
    sender_name = data['sender_name']
    sender_phone = data['sender_phone']
    sender_location = data['sender_location']
    recipient_name = data['recipient_name']
    recipient_phone = data['recipient_phone']
    recipient_location = data['recipient_location']
    parcel = Parcel(sender_name, sender_phone, sender_location, recipient_name, recipient_phone, recipient_location)
    Parcel.addParcel(parcel)

    message = {'parcel':parcel.__repr__(),
               'message':'added successfully'}
    response = jsonify(message)
    response.status_code = 201
    return response
