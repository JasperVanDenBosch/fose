import unittest


class FoseTests(unittest.TestCase):

    def test_version(self):
        import fose
        self.assertNotNone(fose.version)

if __name__ == '__main__':
    unittest.main()
