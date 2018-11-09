from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User (object):
    user_list = []

    def __init__(self, username, email, phone, password):
        self.user_id = len(User.user_list) + 1
        self.username = username
        self.email = email
        self.phone = phone
        self.password_hash = generate_password_hash(password)

    def reset_password(self, new_password):
        new_password_hash = generate_password_hash(new_password)
        self.password_hash = new_password_hash

    def __eq__(self, other):
        return self.email == other.email

    @staticmethod
    def get_user(user_id):
        for user in User.user_list:
            if user.user_id == user_id:
                return user
        return None

    @staticmethod
    def get_user_by_email(email):
        for user in User.user_list:
            if user.email == email:
                return user
        return None

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index >= len(User.user_list) - 1:
            raise StopIteration
        self.__index += 1
        user = User.user_list[self.__index]
        return user

    def __repr__(self):
        return {'user_id':self.user_id,
                'username': self.username,
                'email':self.email,
                'phone':self.phone,
                'password_hash':self.password_hash
                }

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Parcel (object):
    """"Class Description goes here"""
    parcel_list=[]

    def __init__(self, sender_name,sender_phone, sender_location, recipient_name, recipient_phone, recipient_location):
        self.parcel_id = len(Parcel.parcel_list) + 1
        self.sender_name = sender_name
        self.sender_phone = sender_phone
        self.sender_location = sender_location
        self.recipient_name = recipient_name
        self.recipient_phone = recipient_phone
        self.recipient_location = recipient_location
        self.status = "dispatched",
        self.date = datetime.now()


    def changeStatus(self, new_status):
        self.status = new_status
        return self.status

    def changeLocation(self, new_location):
        self.recipient_location = new_location
        return self.recipient_location
    
    @staticmethod
    def addParcel(parcel):
        Parcel.parcel_list.append(parcel)

    @staticmethod
    def removeParcel(parcel_id):
        parcel = Parcel.getParcel(parcel_id)
        Parcel.parcel_list.remove(parcel)

    @staticmethod
    def getParcel(parcel_id):
        for parcel in Parcel.parcel_list:
            if parcel.parcel_id == parcel_id:
                return parcel
        return None

    def __eq__(self, other):
        return self.email == other.email

    def __iter__(self):
        self.__index = -1
        return self

    def __next__(self):
        if self.__index >= len(Parcel.parcel_list) - 1:
            raise StopIteration
        self.__index += 1
        parcel = Parcel.parcel_list[self.__index]
        return parcel

    def __repr__(self):
        return {'parcel_id':self.parcel_id,
                'sender_name': self.sender_name,
                'sender_phone':self.sender_phone,
                'sender_location':self.sender_location,
                'recipient_name':self.recipient_name,
                'recipient_phone':self.recipient_phone,
                'recipient_location':self.recipient_location,
                'parcel_status':self.status,
                'date':str(self.date)
                }
