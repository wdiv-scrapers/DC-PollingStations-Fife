from dc_base_scrapers.xml_scraper import Wfs2Scraper


stations_url = "http://arcgisweb.fife.gov.uk/geoserver/fife/wfs?service=WFS&version=1.3.0&request=GetFeature&typeNames=fife%3APOLLING_PLACES&srsName=EPSG%3A4326"
stations_fields = {
    '{http://arcgisweb.fife.gov.uk/geoserver}CODE': 'CODE',
    '{http://arcgisweb.fife.gov.uk/geoserver}NAME': 'NAME',
    '{http://arcgisweb.fife.gov.uk/geoserver}POLLING_PLACE': 'POLLING_PLACE',
    '{http://arcgisweb.fife.gov.uk/geoserver}OBJECTID': 'OBJECTID',
}

districts_url = "http://arcgisweb.fife.gov.uk/geoserver/fife/wfs?service=WFS&version=1.3.0&request=GetFeature&typeNames=fife%3APOLLING_DISTRICT&srsName=EPSG%3A4326"
districts_fields = {
    '{http://arcgisweb.fife.gov.uk/geoserver}CODE': 'CODE',
    '{http://arcgisweb.fife.gov.uk/geoserver}NAME': 'NAME',
    '{http://arcgisweb.fife.gov.uk/geoserver}POLLING_PLACE': 'POLLING_PLACE',
    '{http://arcgisweb.fife.gov.uk/geoserver}OBJECTID': 'OBJECTID',
}

council_id = 'S12000015'


stations_scraper = Wfs2Scraper(stations_url, council_id, 'stations', stations_fields, 'OBJECTID')
stations_scraper.scrape()
districts_scraper = Wfs2Scraper(districts_url, council_id, 'districts', districts_fields, 'OBJECTID')
districts_scraper.scrape()
