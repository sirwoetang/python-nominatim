Prerequisites
=============

Requires python2.7.x. Initially, you need to install prerequisites (simplejson)

    python setup.py install

Development and Testing
=======================
    python geocodertests.py

Code
====

Reverse Geocode
---------------

    from nominatim import ReverseGeocoder
    client = ReverseGeocoder("http://192.168.10.50/nominatim/reverse.php?format=json")
    response = client.geocode(-37.856206, 145.233980)

    print response['full_address']
    #Amesbury Avenue, Wantirna, City of Knox, 3152, Australia

