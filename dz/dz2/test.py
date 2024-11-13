import unittest
from unittest.mock import patch
from viz_deps import fetch_dependencies, build_graph

class TestDependencyVisualizer(unittest.TestCase):

    @patch('subprocess.run')
    def test_fetch_dependencies(self, mock_run):
        mock_run.return_value.stdout = 'Name: requests\nVersion: 2.25.1\nRequires: certifi, urllib3\n'
        mock_run.return_value.returncode = 0
        dependencies, _ = fetch_dependencies('requests', 1)
        self.assertIn('requests', dependencies)
        self.assertListEqual(dependencies['requests'], ['certifi', 'urllib3'])

    def test_graph_building(self):
        graph = build_graph({'requests': ['certifi', 'urllib3']})
        self.assertIn('requests -> certifi', graph.source)
        self.assertIn('requests -> urllib3', graph.source)

if __name__ == '__main__':
    unittest.main()
