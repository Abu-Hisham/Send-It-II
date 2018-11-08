from werkzeug.security import generate_password_hash, check_password_hash


class User (object):
    user_list = []

    def __init__(self, user_id, username, email, phone, password):
        self.user_id = user_id
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
                'phone':self.phone
                }

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

