from flask import Blueprint, request, jsonify
from app.api.V1.models import Parcel, User

bp = Blueprint('app', __name__, url_prefix='/api/v1')


@bp.route('/')
@bp.route('/index')
def index():
    return "Welcome to send it application!"


@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data['username']
    email = data['email']
    phone = data['phone']
    password = data['password']
    data_error = User.validate_data(username, email, phone, password)

    if data_error == {}:
        user = User(username, email, phone, password)
        if user in User.user_list:
            message = {'user': user.username,
                       'status': 'User Exists'}
            response = jsonify(message)
            response.status_code = 400
            return response
        else:
            User.user_list.append(user)
            message = {'user': user.__repr__(),
                       'status': 'User created successfully'
                       }
            response = jsonify(message)
            response.status_code = 201
            return response
    message = {'error(s)': data_error}
    response = jsonify(message)
    response.status_code = 400
    return response


@bp.route('/parcels', methods=['POST'])
def create_parcel_delivery_order():
    data = request.get_json()
    sender_name = data['sender_name']
    sender_phone = data['sender_phone']
    sender_location = data['sender_location']
    recipient_name = data['recipient_name']
    recipient_phone = data['recipient_phone']
    recipient_location = data['recipient_location']
    data_error = Parcel.validate_data(sender_name, sender_phone, sender_location, recipient_name, recipient_phone, recipient_location)
    if data_error == {}:
        parcel = Parcel(sender_name, sender_phone, sender_location, recipient_name, recipient_phone, recipient_location)
        Parcel.add_parcel(parcel)
        response = jsonify(parcel.__repr__())
        response.status_code = 201
        return response
    else:
        message = {'error(s)': data_error}
        response = jsonify(message)
        response.status_code = 400
        return response


@bp.route('/parcels/<int:parcel_id>', methods=['GET'])
def get_a_specific_parcel(parcel_id, **kwargs):
    parcel = Parcel.get_parcel(parcel_id)
    if parcel is not None:
        message = {"parcel": parcel.__repr__(),
                   "status": "Successfully retrieved"}
        response = jsonify(message)
        response.status_code = 200
        return response
    else:
        message = {
            'Error': "Parcel with the given ID was not found"
        }
        response = jsonify(message)
        response.status_code = 404
        return response


@bp.route('/users/<int:user_id>/parcels', methods=['GET'])
def get_user_parcels(user_id, **kwargs):
    user = User.get_user(user_id)
    if user is not None:
        parcels = Parcel.get_user_parcels(user.phone)
        res = {}
        index = 1
        for parcel in parcels:
            res[index] = parcel.__repr__()
            index += 1
        message = {"parcels": res,
                   "status": "Successfully retrieved"}
        response = jsonify(message)
        response.status_code = 200
        return response
    else:
        message = {'error': "Not a valid user"}
        response = jsonify(message)
        response.status_code = 400
        return response


@bp.route('/parcels', methods=['GET'])
def get_all_parcels():
    parcels = Parcel.parcel_list
    res = {}
    index = 1
    for parcel in parcels:
        res[index] = parcel.__repr__()
        index += 1
    message = {"parcels": res,
               "status": "Successfully retrieved"}
    response = jsonify(message)
    response.status_code = 200
    return response


@bp.route('/parcels/<int:parcel_id>/cancel', methods=['PUT'])
def cancel_a_delivery_order(parcel_id, **kwargs):
    data = request.get_json()
    parcel = Parcel.get_parcel(parcel_id)
    if parcel is not None:
        parcel.status = data['new_status']
        message = {"parcel": parcel.__repr__(),
                   "status": "Successfully Updated"}
        response = jsonify(message)
        response.status_code = 200
        return response
    else:
        response = jsonify({"error": "Resource not found"})
        response.status_code = 404
        return response
