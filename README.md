Installation
=============

Requires python2.7.x for development. Initially, you need to install prerequisites (simplejson) thru setup.py.

    # python setup.py install
    ...
    Installed /usr/local/lib/python2.6/site-packages/

Depending on your PYTHON configuration, setup.py will put files in  /usr/local/lib/pythonx.x/site-packages/

Development and Testing
=======================
    python geocodertests.py

Reverse Geocode
---------------

    from nominatim import ReverseGeocoder
    client = ReverseGeocoder("http://127.0.0.1/nominatim/reverse.php?format=json")
    response = client.geocode(-37.856206, 145.233980)

    print response['full_address']
    #Amesbury Avenue, Wantirna, City of Knox, 3152, Australia

Database Function
---------------

This assumes you have PL/PYTHON installed for Postgres and have run setup.py. See Installation above.

  # createdb -E utf8 testdb
  # psql -d testdb -f setup.sql
  # psql -d testdb
  # SELECT reverse_geocode('http://127.0.0.1/nominatim/reverse.php?format=json', -37.856206, 145.233980); 
                         reverse_geocode
    ----------------------------------------------------------
     Amesbury Avenue, Wantirna, City of Knox, 3152, Australia
    (1 row)
