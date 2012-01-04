CREATE PROCEDURAL LANGUAGE 'plpythonu' HANDLER plpython_call_handler;

CREATE OR REPLACE FUNCTION reverse_geocode(geocoding_url text, latitude float, longitude float) RETURNS
  text
  AS
  $$
    import nominatim
    client = nominatim.ReverseGeocoder(geocoding_url)
    response = client.geocode(latitude, longitude)
    return response['full_address']
  $$
  language 'plpythonu';
