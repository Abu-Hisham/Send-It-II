import unittest

import json
from app import app
from app.api.V1.models import User, Parcel


class SendItTestCase(unittest.TestCase):
    """This class represents the weconnect Testcase"""

    def setUp(self):
        """Define variables and initialize app."""
        self.client = app.test_client()
        self.client.testing = True
        self.parcel_list = []
        self.user_list = []
        self.parcel_data1 = {
            'sender_name': "Abdul",
            'sender_phone': "0701633016",
            'sender_location': "Madaraka",
            'recipient_name': "Zahry",
            'recipient_phone': "0702733016",
            'recipient_location': "Kileleshwa"
        }
        self.user_data1 = {
            'username': "Abdul",
            'email': "abdul@gmail.com",
            'phone': "0701633016",
            'password': "mypass"
        }
        self.parcel_data2 = {
            'sender_name': "Zahry",
            'sender_phone': "0702733016",
            'sender_location': "Kileleshwa",
            'recipient_name': "Abdul",
            'recipient_phone': "0701633016",
            'recipient_location': "Madaraka"
        }

    def test_get_a_single_parcel(self):
        self.client.post('/api/v1/parcels', data=json.dumps(self.parcel_data1),
                         headers={'content-type': 'application/json'})
        parcel = Parcel.parcel_list[0]

        res = self.client.get('/api/v1/parcels/' + str(parcel.parcel_id),
                              headers={'content-type': 'application/json'})
        self.assertIn(parcel, Parcel.parcel_list)
        self.assertIn(parcel.__repr__()['sender_name'], str(res.data))
        self.assertEqual(res.status_code, 200)

    def test_get_all_parcels(self):
        parcel1 = self.client.post('/api/v1/parcels', data=json.dumps(self.parcel_data1),
                         headers={'content-type': 'application/json'})

        parcel2 = self.client.post('/api/v1/parcels', data=json.dumps(self.parcel_data2),
                         headers={'content-type': 'application/json'})
        res = self.client.get('/api/v1/parcels',
                              headers={'content-type': 'application/json'})
        self.assertIn(parcel1.sender_name,res.data)
        self.assertIn(parcel2.sender_name,res.data)
        self.assertEqual(res.status_code, 200)

    def test_cancel_delivery_order(self):
        self.client.post('/api/v1/parcels', data=json.dumps(self.parcel_data2),
                         headers={'content-type': 'application/json'})
        data = {'new_status': "cancelled"}
        res = self.client.put('/api/v1/parcels/1/cancel', data=json.dumps(data),
                              headers={'content-type': 'application/json'})

        self.assertEqual(res.status_code, 200)

    def test_get_all_parcels(self):
        pass

    def test_fetch_parcel_delivery_orders_for_a_user(self):
        self.client.post('/api/v1/users', data=json.dumps(self.user_data1),
                         headers={'content-type': 'application/json'})
        self.parcel_data1['sender_phone'] = self.user_data1['phone']
        self.client.post('/api/v1/parcels', data=json.dumps(self.parcel_data1),
                         headers={'content-type': 'application/json'})
        res = self.client.get('/api/v1/users/1/parcels',
                              headers={'content-type': 'application/json'})
        self.assertEqual(res.status_code, 200)

    def test_cancel_parcel_delivery_order(self):
        pass

    def test_create_parcel_delivery_order(self):
        res = self.client.post('/api/v1/parcels', data=json.dumps(self.parcel_data1),
                               headers={'content-type': 'application/json'})
        self.assertEqual(res.status_code, 201)

    def test_create_user(self):
        res = self.client.post('/api/v1/users', data=json.dumps(self.user_data1),
                               headers={'content-type': 'application/json'})
        self.assertEqual(res.status_code, 201)
        self.assertIn(self.user_data1['username'], str(res.data))


if __name__ == "__main__":
    unittest.main()
