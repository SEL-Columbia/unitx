import unittest
from unitx import run_main


class UnitxTests(unittest.TestCase):
    """
    Tests for core functions of unitx
    """
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
        self.assertEqual(cm['classification']['name'],
                         'consummer-message-alphabetical')

    def test_run_main(self):
        msg = run_main(self.get_raw_message())
        self.assertIsInstance(msg, dict)


class UnitxConsumerTestMessage(unittest.TestCase):
    """
    Lets test all of the messages we have
    """
    def setUp(self):
        """
        """

    def test_balance(self):
        msg = run_main('body=bal.1234')
        self.assertEqual(
            msg['classification']['name'], 'consummer-message-alphabetical')
        self.assertEqual(
            msg['route']['name'], 'check_circuit_balance')

    def test_balance_numeric(self):
        msg = run_main('body=2.1234')
        self.assertEqual(
            msg['classification']['name'], 'consumer-message-numeric')
        self.assertEqual(
            msg['route']['name'], 'check_circuit_balance')

    def test_balance_french(self):
        msg = run_main('body=solde.1234')
        self.assertEqual(
            msg['classification']['name'], 'consummer-message-alphabetical')
        self.assertEqual(msg['route']['name'],
                         'check_circuit_balance')


class UnitxMeterMessagesTest(unittest.TestCase):
    """
    Tests for meter messages
    """
    def setUP(self):
        """
        """
