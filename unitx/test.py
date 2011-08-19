import unittest


class UnitxTests(unittest.TestCase):

    def setUp(self):
        """
        """

    def get_raw_message(self):
        return 'address=18182124554&body=bal.12345'

    def get_parsed(self):
        from unitx import initial_parse
        return initial_parse(self.get_raw_message())

    def test_load_config(self):
        from unitx import load_config
        config = load_config('config.yaml')
        self.assertIsInstance(config, dict)

    def test_initial_parse(self):
        m = self.get_parsed()
        self.assertIsInstance(m, dict)
        self.assertEqual(m['body'], 'bal.12345')
        self.assertEqual(m['address'], '18182124554')

    def test_classify(self):
        """
        """
        from unitx import classify
        cm = classify(self.get_parsed())
        self.assertEqual(cm['classification'],
                         'consummer-message-alphabetical')
