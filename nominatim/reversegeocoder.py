import urllib
import urllib2
import simplejson

class ReverseGeocoder(object):
    def __init__(self, base_url = "http://open.mapquestapi.com/nominatim/v1/reverse?format=json"):
        self.base_url = base_url + "&%s"

    def geocode(self, lat, lon, zoom, addressdetails=1):
        
        params = { 'lat' : lat }
        params['lon'] = lon
        params['zoom'] = zoom
        params['addressdetails'] = addressdetails

        url = self.base_url % urllib.urlencode(params)
        data = urllib2.urlopen(url)
        response = data.read()
        
        return self.parse_json(response)

    def parse_json(self, data):
        try:
            data = simplejson.loads(data)
        except simplejson.JSONDecodeError:
            data = []
        
        return data
