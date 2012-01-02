Prerequisites
=============

Requires python2.7.x. Initially, you need to install prerequisites (simplejson)

    python setup.py install

Development and Testing
=======================
    python geocodertests.py

Sample Code
===========

Reverse Geocode
---------------

    from nominatim import ReverseGeocoder
    client = ReverseGeocoder("http://127.0.0.1/nominatim/reverse.php?format=json")
    response = client.geocode(-37.856206, 145.233980)

    print response['full_address']
    #Amesbury Avenue, Wantirna, City of Knox, 3152, Australia

Database Function
---------------

    CREATE OR REPLACE FUNCTION reverse_geocode(latitude float, longitude float) RETURNS
         text
    AS
    $$
     import nominatim
     client = nominatim.ReverseGeocoder("http://127.0.0.1/nominatim/reverse.php?format=json")
     response = client.geocode(latitude, longitude)
     return response['full_address']
    $$
    language 'plpythonu';

    # SELECT reverse_geocode(-37.856206, 145.233980);
                         reverse_geocode
    ----------------------------------------------------------
     Amesbury Avenue, Wantirna, City of Knox, 3152, Australia
    (1 row)


