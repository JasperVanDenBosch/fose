import unittest, sys
from fose.protocol import UriBuilder


def runtest(testclass):
    suite = unittest.TestLoader().loadTestsFromTestCase(testclass)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
    if not testResult.wasSuccessful():
        sys.exit('[fose test wrapper] One or more tests failed!')


class ComplianceTests(unittest.TestCase):

    def setUp(self):
        self.uri = UriBuilder(self.rootUrl)

    def test_Get_reviews_for_id(self):
		#use protocol url to GET response 
        url = self.uri.forDoi('fosetest.1')
		#test schema validation
		#use core lib to read this as a model object
		#test for properties
        self.fail('Running compliance tests on url: {0} '.format(url))

def run(targetUrl):
    ComplianceTests.rootUrl = targetUrl
    runtest(ComplianceTests)

if __name__ == '__main__':
    unittest.main()
