import unittest, sys


def runtest(testclass):
    suite = unittest.TestLoader().loadTestsFromTestCase(testclass)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
    if not testResult.wasSuccessful():
        sys.exit('[fose test wrapper] One or more tests failed!')


class ComplianceTests(unittest.TestCase):

    def test_sth(self):
        self.fail('Running compliance tests on url: {0} '.format(self.rootUrl))

def run(targetUrl):
    ComplianceTests.rootUrl = targetUrl
    runtest(ComplianceTests)

if __name__ == '__main__':
    unittest.main()
