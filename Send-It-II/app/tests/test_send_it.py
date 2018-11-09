import unittest

import json
from app import app
from app.api.V1.models import User, Parcel


class WeconnectTestCase (unittest.TestCase):
    """This class represents the weconnect Testcase"""

    def setUp(self):
        """Define variables and initialize app."""
        self.client = app.test_client ()
        self.client.testing = True
        self.parcel_list = []
        self.user_list = []
        self.user1 = User(1,"Abdul","abdul@gmail.com","0701633016","mypass")
        self.user2 = User(2,"Zahry","zahry@gmail.com","0702733016","mypass")
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
        pass
if __name__ == "__main__":
    unittest.main()