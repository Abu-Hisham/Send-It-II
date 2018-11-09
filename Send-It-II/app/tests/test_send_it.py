import unittest

import json
from app import app
from app.api.V1.models import User, Parcel


class SendItTestCase (unittest.TestCase):
    """This class represents the weconnect Testcase"""

    def setUp(self):
        """Define variables and initialize app."""
        self.client = app.test_client ()
        self.client.testing = True
        self.parcel_list = []
        self.user_list = []
        # self.user1 = User(1,"Abdul","abdul@gmail.com","0701633016","mypass")
        # self.user2 = User(2,"Zahry","zahry@gmail.com","0702733016","mypass")
        self.parcel1 = Parcel("Abdul","0701633016","Madaraka","Zahry","0702733016","Kileleshwa")
        self.parcel2 = Parcel("Zahry", "0702733016", "Kileleshwa", "Abdul", "0701633016", "Madaraka")
    def test_get_a_single_parcel(self):
        pass
    def test_get_all_parcels(self):
        pass
    def test_fetch_parcel_delivery_orders_for_a_user(self):
        pass
    def test_cancel_parcel_delivery_order(self):
        pass
    def test_create_parcel_delivery_order(self):
        parcel_data = self.parcel1.__repr__()
        res = self.client.post('/api/v1/parcels', data=json.dumps(parcel_data),
                               headers={'content-type': 'application/json'})
        self.assertEqual(res.status_code, 201)

    def test_create_user(self):
        user_data = {
                        'username': "Abdul",
                        'email':"abdul@gmail.com",
                        'phone': "0701633016",
                        'password':"mypass"
                    }
        res = self.client.post('/api/v1/users', data=json.dumps(user_data),
                               headers={'content-type': 'application/json'})
        self.assertEqual(res.status_code, 201)
        self.assertIn(user_data['username'], str(res.data))

if __name__ == "__main__":
    unittest.main()