import unittest
from viz_deps import strip_version  # Убедитесь, что импортируете вашу функцию правильно

class TestStripVersion(unittest.TestCase):

    def test_basic_dependency(self):
        self.assertEqual(strip_version('requests'), 'requests')

    def test_simple_version(self):
        self.assertEqual(strip_version('requests>=2.0.0'), 'requests')

    def test_extra(self):
        self.assertEqual(strip_version('requests[security]'), 'requests')

    def test_version_with_extra(self):
        self.assertEqual(strip_version('requests[security]>=2.0.0'), 'requests')

    def test_complex_requirements(self):
        self.assertEqual(strip_version('some-package; os_version == "Linux"'), 'some-package')

    def test_multiple_conditions(self):
        self.assertEqual(strip_version('some-package; python_version < "3.8"'), 'some-package')

    def test_ignore_version_with_conditions(self):
        self.assertEqual(strip_version('requests<3.0; python_version >= "3.6"'), 'requests')

    def test_empty_string(self):
        self.assertEqual(strip_version(''), '')

    def test_white_space(self):
        self.assertEqual(strip_version('   requests   '), 'requests')

if __name__ == '__main__':
    unittest.main()
