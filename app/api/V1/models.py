from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class User(object):
    user_list = []

    def __init__(self, username, email, phone, password):
        """
        :param username:
        :param email:
        :param phone:
        :param password:
        """
        self.user_id = len(User.user_list) + 1
        self.username = username
        self.email = email
        self.phone = phone
        self.password_hash = generate_password_hash(password)

    def reset_password(self, new_password):
        """
        Resets the user passwordhash using the passed parameter

        Args:
        :param new_password: new password value
        :return: None
        """
        new_password_hash = generate_password_hash(new_password)
        self.password_hash = new_password_hash

    def __eq__(self, other):
        return self.email == other.email

    @staticmethod
    def get_user(user_id):
        """
         Class method for fetching a specific user using ID

        :param user_id: ID for the specific user
        :return:  User Object(if user with the email exists,
                None if no user with the email exists
        """
        for user in User.user_list:
            if user.user_id == user_id:
                return user
        return None

    @staticmethod
    def get_user_by_email(email):
        """
        Class method for fetching a specific user using email
        :param email: email of the specific user
        :return: User Object(if user with the email exists,
                None if no user with the email exists
        """
        for user in User.user_list:
            if user.email == email:
                return user
        return None

    def check_password(self, password):
        """
        Class method for verifying user password
        :param password: user password
        :return: True if password is valid,
                False if invalid
        """
        return check_password_hash(self.password_hash, password)

    def __iter__(self):
        """
        Class method for initializing index for object iteration

        :return: current object in the current iteration
        """
        self.__index = -1
        return self

    def __next__(self):
        """
        Class method for passing the next object in iteration

        :return: the next object in iteration
        """
        if self.__index >= len(User.user_list) - 1:
            raise StopIteration
        self.__index += 1
        user = User.user_list[self.__index]
        return user

    def __repr__(self):
        """
        Class method for formatting object representation
        :return: Formatted Dictionary
        """
        return {'user_id': self.user_id,
                'username': self.username,
                'email': self.email,
                'phone': self.phone,
                'password_hash': self.password_hash
                }


class Parcel(object):
    """"Class for template for parcel object"""

    parcel_list = []

    def __init__(self, sender_name, sender_phone, sender_location, recipient_name, recipient_phone, recipient_location):
        """
        Constructor method of the class

        :param sender_name: Name of the sender
        :param sender_phone: contact of the sender
        :param sender_location: Location of the sender
        :param recipient_name: Name of the recipient
        :param recipient_phone: Contact of the recipient
        :param recipient_location: location of the recipient
        """
        self.parcel_id = len(Parcel.parcel_list) + 1
        self.sender_name = sender_name
        self.sender_phone = sender_phone
        self.sender_location = sender_location
        self.recipient_name = recipient_name
        self.recipient_phone = recipient_phone
        self.recipient_location = recipient_location
        self.status = "dispatched",
        self.date = datetime.now()

    def change_status(self, new_status):
        """
        Object method for changing status of the parcel

        :param new_status: New status
        :return: The changed status
        """
        self.status = new_status
        return self.status

    @staticmethod
    def add_parcel(parcel):
        """
        A class method for adding parcel to the parcel list

        :param parcel: parcel object
        :return: Null
        """
        Parcel.parcel_list.append(parcel)

    @staticmethod
    def remove_parcel(parcel_id):
        """
        A class method for removing parcel to the parcel list

        :param parcel_id:
        :return: Null
        """
        parcel = Parcel.getParcel(parcel_id)
        Parcel.parcel_list.remove(parcel)

    @staticmethod
    def get_parcel(parcel_id):
        """
        Class method for getting parcel using parcel ID
        :param parcel_id: ID of the specific parcel
        :return: parcel, if a parcel with the ID exists
                 None, if No parcel with the ID exists
        """
        for parcel in Parcel.parcel_list:
            if parcel.parcel_id == parcel_id:
                return parcel
        return None

    @staticmethod
    def get_user_parcels(user_phone):
        """
        Class method for getting parcels belonging to a user

        :param user_phone: Contact of the user
        :return: List of parcels belonging to the user
        """
        user_parcels = []
        for parcel in Parcel.parcel_list:
            if parcel.sender_phone == user_phone:
                user_parcels.append(parcel)
        return user_parcels

    def __eq__(self, other):
        """
        Class method for comparing objects created from it
        :param other: Arbitrary object belonging to this class
        :return: object of the class
        """
        return self.email == other.email

    def __iter__(self):
        """
        Class method for initializing index for object iteration

        :return: current object in the current iteration
        """
        self.__index = -1
        return self

    def __next__(self):
        """
        Class method for passing the next object in iteration

        :return: the next object in iteration
        """
        if self.__index >= len(Parcel.parcel_list) - 1:
            raise StopIteration
        self.__index += 1
        parcel = Parcel.parcel_list[self.__index]
        return parcel

    def __repr__(self):
        """
        Class method for formatting object representation

        :return: Formatted Dictionary
        """
        return {'parcel_id': self.parcel_id,
                'sender_name': self.sender_name,
                'sender_phone': self.sender_phone,
                'sender_location': self.sender_location,
                'recipient_name': self.recipient_name,
                'recipient_phone': self.recipient_phone,
                'recipient_location': self.recipient_location,
                'parcel_status': self.status,
                'date': str(self.date)
                }
