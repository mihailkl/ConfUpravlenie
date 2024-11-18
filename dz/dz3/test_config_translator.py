import unittest
from config_translator import evaluate_expression, translate_to_custom_config

class TestConfigTranslator(unittest.TestCase):
    def test_evaluate_expression(self):
        context = {'x': 10, 'y': 20}
        self.assertEqual(evaluate_expression("#[+ x y]", context), 30)
        self.assertEqual(evaluate_expression("#[min x y]", context), 10)
        self.assertEqual(evaluate_expression("#[max x y]", context), 20)

    def test_translate_to_custom_config(self):
        data = {
            'count': "#[+ 1 2]",
            'maximum': "#[max 10 20 30]",
            'minimum': "#[min 100 50 25]"
        }
        output = translate_to_custom_config(data)
        self.assertIn("global count = 3", output)
        self.assertIn("global maximum = 30", output)
        self.assertIn("global minimum = 25", output)

if __name__ == "__main__":
    unittest.main()