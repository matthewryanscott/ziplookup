from simplejson import loads

from ziplookup.tests import *


class TestLookupController(TestController):

    def test_good(self):
        response = self.app.get(url_for(controller='lookup', zipcode='98230'))
        assert loads(response.body) == dict(city='Blaine', state='WA')
        content_type = response.header_dict['content-type']
        assert content_type.startswith('application/json')
