import unittest
from unittest.mock import patch
from viz_deps import fetch_dependencies, build_dot_representation

class TestDependencyVisualizer(unittest.TestCase):

    @patch('subprocess.run')
    def test_fetch_dependencies(self, mock_run):
        mock_run.return_value.stdout = 'Name: requests\nVersion: 2.25.1\nRequires: certifi, urllib3\n'
        mock_run.return_value.returncode = 0
        dependencies, _ = fetch_dependencies('requests', 1)
        self.assertIn('requests', dependencies)
        self.assertListEqual(dependencies['requests'], ['certifi', 'urllib3'])

    def test_dot_representation_building(self):
        dot_content = build_dot_representation({'requests': ['certifi', 'urllib3']})
        expected_content = (
            'digraph {\n'
            '    "requests" -> "certifi"\n'
            '    "requests" -> "urllib3"\n'
            '}\n'
        )
        self.assertEqual(dot_content, expected_content)

if __name__ == '__main__':
    unittest.main()
