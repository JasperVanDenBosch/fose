import unittest

def runtest(testclass):
    suite = unittest.TestLoader().loadTestsFromTestCase(testclass)
    testResult = unittest.TextTestRunner(verbosity=2).run(suite)
    if not testResult.wasSuccessful():
        sys.exit('[fexpect test wrapper] One or more tests failed!')

def runall():
    runtest(FoseTests)

class FoseTests(unittest.TestCase):

    def test_version(self):
        import fose
        import pkg_resources
        pkgversion = pkg_resources.get_distribution("fose").version
        self.assertEqual(fose.version,pkgversion)

def run():
    unittest.main()

if __name__ == '__main__':
    unittest.main()
