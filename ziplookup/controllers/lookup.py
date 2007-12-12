import logging

from ziplookup.data.zipcode import get_zipcode_info
from ziplookup.lib.base import *

log = logging.getLogger(__name__)

class LookupController(BaseController):

    def index(self, zipcode):
        response.headers['content-type'] = 'application/json; charset=utf-8'
        return get_zipcode_info(str(zipcode))
