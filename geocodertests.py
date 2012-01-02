import nominatim
import unittest

class GeocoderTestCase(unittest.TestCase):

    def test_geocode_city(self):
        client = nominatim.Geocoder("http://open.mapquestapi.com/nominatim/v1/search?format=json")
        response = client.geocode('Hays, Kansas')
        self.assertIsNotNone(response)

    def test_reverse_geocode(self):
        client = nominatim.ReverseGeocoder("http://127.0.0.1/nominatim/reverse.php?format=json")
        response = client.geocode(-38.02183, 145.23557)
        self.assertIsNotNone(response)
        self.assertIsNotNone(response['full_address'])

    def test_reverse_geocode_no_result(self):
        client = nominatim.ReverseGeocoder("http://127.0.0.1/nominatim/reverse.php?format=json")
        response = client.geocode(-90.02183, 145.23557)
        self.assertIsNotNone(response)
        self.assertIsNotNone(response['full_address'])

if __name__ == "__main__":
    unittest.main()

