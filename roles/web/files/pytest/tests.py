import pytest
import requests
requests.packages.urllib3.disable_warnings()

from pages.page import Page

nondestructive = pytest.mark.nondestructive


@nondestructive
class Test(object):

    @pytest.mark.stat
    def test_pdp_status(self, mozwebqa):
        browser = Page(mozwebqa)
        browser.open('')
        browser.take_screenshot('reddit')
