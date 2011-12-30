import urllib
import urllib2
import simplejson

class ReverseGeocoder(object):
    def __init__(self, base_url = "http://open.mapquestapi.com/nominatim/v1/reverse?format=json"):
        self.base_url = base_url + "&%s"

    def geocode(self, lat, lon):
        
        params = { 'lat' : lat , 'lon' : lon}

        url = self.base_url % urllib.urlencode(params)
        data = urllib2.urlopen(url)
        response = data.read()
        
        return self.parse_json(response)

    def parse_json(self, data):
        try:
            data = simplejson.loads(data)
            data['full_address'] = data['display_name']
        except simplejson.JSONDecodeError:
            data = []
        
        return data
