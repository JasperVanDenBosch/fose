import unittest, sys
from fose.protocol import UriBuilder
import pkg_resources
from lxml import etree
import requests


def runtest(testclass):
    suite = unittest.TestLoader().loadTestsFromTestCase(testclass)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
    if not testResult.wasSuccessful():
        sys.exit('[fose test wrapper] One or more tests failed!')


class ComplianceTests(unittest.TestCase):

    def setUp(self):
        self.uri = UriBuilder(self.rootUrl)

    def test_Get_review_thread_for_id(self):
		#use protocol url to GET response 
        url = self.uri.forDoi('fosetest.1')
        #actually get file
        response = requests.get(url, headers={'Accept':'application/xml'})
        response.raise_for_status()
		#test schema validation
        schemaFilename = pkg_resources.resource_filename('fose','thread.xsd')
        schema = etree.XMLSchema(file=schemaFilename)
        parser = etree.XMLParser(schema = schema)
        #THREAD = '<?xml version="1.0"?><thread xmlns="http://fose1.org/fose"/>'
        root = etree.fromstring(response.text, parser)
		#use core lib to read this as a model object
		#test for properties
        self.fail('Running compliance tests on url: {0} '.format(url))

def run(targetUrl):
    ComplianceTests.rootUrl = targetUrl
    runtest(ComplianceTests)

if __name__ == '__main__':
    unittest.main()
