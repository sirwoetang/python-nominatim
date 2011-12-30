import nominatim
import unittest

class GeocoderTestCase(unittest.TestCase):

    def test_geocode_city(self):
        client = nominatim.Geocoder("http://open.mapquestapi.com/nominatim/v1/search?format=json")
        response = client.geocode('Hays, Kansas')
        self.assertIsNotNone(response)

    def test_reverse_geocode(self):
        client = nominatim.ReverseGeocoder("http://192.168.10.50/nominatim/reverse.php?format=json")
        response = client.geocode(-38.02183, 145.23557, 18, 1)
        self.assertIsNotNone(response)
        self.assertIsNotNone(response['full_address'])

if __name__ == "__main__":
    unittest.main()

