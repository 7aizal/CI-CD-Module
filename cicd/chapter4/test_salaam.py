import unittest

from hello import say_salaam

class TestSalaam(unittest.TestCase):
    def test_say_salaam(self):
        self.assertEqual(say_salaam(), "Asalamualaikum, World!")

