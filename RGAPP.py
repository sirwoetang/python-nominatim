__author__ = 'Waldo'

import nominatim


def process_file(name):
    input_csv_path = datafile_path(name)
    output_csv_path = datafile_path('output.csv')
    import csv
    row_counter = 0
    with open(input_csv_path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        writer=csv.writer(open(output_csv_path,'wb'))
        next(reader, None)  # skip the headers
        for row in reader:
            row_counter = row_counter + 1
            print(row_counter)
            lat = row[0]
            lon = row[1]
            response = get_address(lat,lon)
            address = json_to_obj(json.dumps(response['address']))
            if hasattr(address, 'road'):
                address.road = 1
            else:
                address.road = 0

            if hasattr(address, 'suburb'):
                address.suburb = 1
            else:
                address.suburb = 0

            if hasattr(address, 'town'):
                address.town = 1
            else:
                address.town = 0

            if hasattr(address, 'city'):
                address.city = 1
            else:
                address.city = 0

            if hasattr(address, 'country'):
                address.country = 1
            else:
                address.country = 0


            from unicodedata import normalize
            full_address = normalize('NFKD', response['full_address']).encode('ASCII', 'ignore')
            full_response =normalize('NFKD', unicode(response)).encode('ASCII', 'ignore')

            writer.writerow([lat, lon, full_address, address.road,address.suburb,address.town, address.city, address.country,full_response] )


def get_address(lat, lon):
    client = nominatim.ReverseGeocoder("")
    response = client.geocode(lat, lon)
    print(response['full_address'])
    return response


def datafile_path(name):
    import os
    return os.path.join(os.path.dirname(__file__), name)


import json

def json_to_obj(s):
    def h2o(x):
        if isinstance(x, dict):
            return type('jo', (), {k: h2o(v) for k, v in x.iteritems()})
        else:
            return x
    return h2o(json.loads(s))


process_file('geolocation.csv')