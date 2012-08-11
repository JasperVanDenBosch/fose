import unittest, sys

def runtest(testclass):
    suite = unittest.TestLoader().loadTestsFromTestCase(testclass)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
    if not testResult.wasSuccessful():
        sys.exit('[fose test wrapper] One or more tests failed!')

def runall():
    runtest(FoseTests)

class FoseTests(unittest.TestCase):

    def test_version(self):
        import fose
        import pkg_resources
        pkgversion = pkg_resources.get_distribution("fose").version
        self.assertEqual(fose.version,pkgversion)

    def test_uribuilder_single_publication_by_doi(self):
        from fose.protocol import UriBuilder
        expected = 'http://base.domain/doi/abc.1234'
        uriBuilder = UriBuilder('http://base.domain')
        self.assertEqual(expected, uriBuilder.forDoi('abc.1234'))

if __name__ == '__main__':
    unittest.main()
