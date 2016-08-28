from geojson_scraper import scrape


stations_url = "http://arcgisweb.fife.gov.uk/geoserver/fife/wfs?service=WFS&version=1.3.0&request=GetFeature&typeNames=fife%3APOLLING_PLACES&outputFormat=json&srsName=EPSG%3A4326"
districts_url = "http://arcgisweb.fife.gov.uk/geoserver/fife/wfs?service=WFS&version=1.3.0&request=GetFeature&typeNames=fife%3APOLLING_DISTRICT&outputFormat=json&srsName=EPSG%3A4326"
council_id = 'S12000015'


scrape(stations_url, council_id, 'utf-8', 'stations')
scrape(districts_url, council_id, 'utf-8', 'districts')
