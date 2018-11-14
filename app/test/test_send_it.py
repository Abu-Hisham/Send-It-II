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
            'sender_name': "AbdulZizu",
            'sender_phone': "0701633016",
            'sender_location': "Madaraka",
            'recipient_name': "AminaZahry",
            'recipient_phone': "0702733016",
            'recipient_location': "Kileleshwa"
        }
        self.user_data1 = {
            'username': "AbdulZizu",
            'email': "abdul@gmail.com",
            'phone': "0701633016",
            'password': "mypass1"
        }
        self.parcel_data2 = {
            'sender_name': "AminaZahry",
            'sender_phone': "0702733016",
            'sender_location': "Kileleshwa",
            'recipient_name': "AbdulZizu",
            'recipient_phone': "0701633016",
            'recipient_location': "Madaraka"
        }

    def test_get_a_single_parcel(self):
        request_data = self.parcel_data1
        self.client.post('/api/v1/parcels', data=json.dumps(request_data),
                         headers={'content-type': 'application/json'})
        parcel = Parcel.parcel_list[0]

        res = self.client.get('/api/v1/parcels/' + str(parcel.parcel_id),
                              headers={'content-type': 'application/json'})
        self.assertIn(parcel, Parcel.parcel_list)
        self.assertIn(parcel.__repr__()['sender_name'], str(res.data))
        self.assertEqual(res.status_code, 200)

    def test_get_all_parcels(self):
        request_data1 = self.parcel_data1
        request_data2 = self.parcel_data2
        self.client.post('/api/v1/parcels', data=json.dumps(request_data1),
                         headers={'content-type': 'application/json'})

        self.client.post('/api/v1/parcels', data=json.dumps(request_data2),
                         headers={'content-type': 'application/json'})
        res = self.client.get('/api/v1/parcels',
                              headers={'content-type': 'application/json'})
        self.assertIn(request_data1['sender_name'], str(res.data))
        self.assertIn(request_data2['sender_name'], str(res.data))
        self.assertEqual(res.status_code, 200)

    def test_cancel_delivery_order(self):
        request_data = self.parcel_data1
        self.client.post('/api/v1/parcels', data=json.dumps(request_data),
                         headers={'content-type': 'application/json'})
        request_data2 = {'new_status': "cancelled"}
        res = self.client.put('/api/v1/parcels/' + str(Parcel.parcel_list[0].parcel_id) + '/cancel',
                              data=json.dumps(request_data2),
                              headers={'content-type': 'application/json'})

        self.assertEqual(res.status_code, 200)
        self.assertIn(request_data2['new_status'], str(res.data))

    def test_fetch_parcel_delivery_orders_for_a_user(self):
        request_data1 = self.user_data1
        request_data2 = self.parcel_data1
        self.client.post('/api/v1/users', data=json.dumps(request_data1),
                         headers={'content-type': 'application/json'})
        request_data2['sender_phone'] = self.user_data1['phone']
        self.client.post('/api/v1/parcels', data=json.dumps(request_data2),
                         headers={'content-type': 'application/json'})
        res = self.client.get('/api/v1/users/' + str(User.user_list[0].user_id) + '/parcels',
                              headers={'content-type': 'application/json'})
        self.assertIn(request_data1['phone'], str(res.data))
        self.assertEqual(res.status_code, 200)

    def test_create_parcel_delivery_order(self):
        request_data = self.parcel_data1
        res = self.client.post('/api/v1/parcels', data=json.dumps(request_data),
                               headers={'content-type': 'application/json'})
        self.assertIn(request_data['sender_name'], str(res.data))
        self.assertEqual(res.status_code, 201)

    def test_invalid_sender_or_recipient_name(self):
        request_data = self.parcel_data1
        request_data['sender_name'] = " "
        res1 = self.client.post('/api/v1/parcels', data=json.dumps(request_data),
                                headers={'content-type': 'application/json'})
        request_data['sender_name'] = "ABC"
        res2 = self.client.post('/api/v1/parcels', data=json.dumps(request_data),
                                headers={'content-type': 'application/json'})
        request_data['recipient_name'] = " "
        res3 = self.client.post('/api/v1/parcels', data=json.dumps(request_data),
                                headers={'content-type': 'application/json'})
        request_data['recipient_name'] = "ABC"
        res4 = self.client.post('/api/v1/parcels', data=json.dumps(request_data),
                                headers={'content-type': 'application/json'})

        error_list = [res1, res2, res3, res4]
        for res in error_list:
            self.assertEqual(res.status_code, 400)
            self.assertIn("error", str(res.data))

    def test_invalid_sender_or_recipient_location(self):
        request_data = self.parcel_data1
        request_data['sender_location'] = " "
        res1 = self.client.post('/api/v1/parcels', data=json.dumps(request_data),
                                headers={'content-type': 'application/json'})
        request_data['sender_location'] = "ABC"
        res2 = self.client.post('/api/v1/parcels', data=json.dumps(request_data),
                                headers={'content-type': 'application/json'})
        request_data['recipient_location'] = " "
        res3 = self.client.post('/api/v1/parcels', data=json.dumps(request_data),
                                headers={'content-type': 'application/json'})
        request_data['recipient_location'] = "ABC"
        res4 = self.client.post('/api/v1/parcels', data=json.dumps(request_data),
                                headers={'content-type': 'application/json'})

        error_list = [res1, res2, res3, res4]
        for res in error_list:
            self.assertEqual(res.status_code, 400)
            self.assertIn("error", str(res.data))

    def test_invalid_sender_or_recipient_phone(self):
        request_data = self.parcel_data1
        request_data['sender_phone'] = "0712"
        res1 = self.client.post('/api/v1/parcels', data=json.dumps(request_data),
                                headers={'content-type': 'application/json'})
        request_data['sender_phone'] = "07123456789"
        res2 = self.client.post('/api/v1/parcels', data=json.dumps(request_data),
                                headers={'content-type': 'application/json'})
        request_data['sender_phone'] = "abcd"
        res3 = self.client.post('/api/v1/parcels', data=json.dumps(request_data),
                                headers={'content-type': 'application/json'})
        request_data['recipient_phone'] = "07123456789"
        res4 = self.client.post('/api/v1/parcels', data=json.dumps(request_data),
                                headers={'content-type': 'application/json'})
        request_data['recipient_phone'] = "0712"
        res5 = self.client.post('/api/v1/parcels', data=json.dumps(request_data),
                                headers={'content-type': 'application/json'})
        request_data['recipient_phone'] = "abcd"
        res6 = self.client.post('/api/v1/parcels', data=json.dumps(request_data),
                                headers={'content-type': 'application/json'})

        error_list = [res1, res2, res3, res4, res5, res6]
        for res in error_list:
            self.assertEqual(res.status_code, 400)
            self.assertIn("error", str(res.data))

    def test_create_user(self):
        request_data = self.user_data1
        res = self.client.post('/api/v1/users', data=json.dumps(request_data),
                               headers={'content-type': 'application/json'})
        self.assertEqual(res.status_code, 201)
        self.assertIn(request_data['username'], str(res.data))

    def test_invalid_username_rejected(self):
        request_data = self.user_data1
        request_data['username'] = ""
        res1 = self.client.post('/api/v1/users', data=json.dumps(request_data),
                                headers={'content-type': 'application/json'})
        request_data['username'] = "123456789"
        res2 = self.client.post('/api/v1/users', data=json.dumps(request_data),
                                headers={'content-type': 'application/json'})
        request_data['username'] = "ABC"
        res3 = self.client.post('/api/v1/users', data=json.dumps(request_data),
                                headers={'content-type': 'application/json'})
        error_list = [res1, res2, res3]
        for res in error_list:
            self.assertEqual(res.status_code, 400)
            self.assertIn("error", str(res.data))

    def test_invalid_email_rejected(self):
        request_data = self.user_data1
        request_data['email'] = "andela.com"
        res1 = self.client.post('/api/v1/users', data=json.dumps(request_data),
                                headers={'content-type': 'application/json'})
        request_data['email'] = "andela"
        res2 = self.client.post('/api/v1/users', data=json.dumps(request_data),
                                headers={'content-type': 'application/json'})
        request_data['email'] = "andela@com"
        res3 = self.client.post('/api/v1/users', data=json.dumps(request_data),
                                headers={'content-type': 'application/json'})
        error_list = [res1, res2, res3]
        for res in error_list:
            self.assertEqual(res.status_code, 400)
            self.assertIn("error", str(res.data))

    def test_invalid_phone_rejected(self):
        request_data = self.user_data1
        request_data['phone'] = "0712"
        res1 = self.client.post('/api/v1/users', data=json.dumps(request_data),
                                headers={'content-type': 'application/json'})
        request_data['phone'] = "07123456789"
        res2 = self.client.post('/api/v1/users', data=json.dumps(request_data),
                                headers={'content-type': 'application/json'})
        error_list = [res1, res2]
        for res in error_list:
            self.assertEqual(res.status_code, 400)
            self.assertIn("error", str(res.data))


if __name__ == "__main__":
    unittest.main()
