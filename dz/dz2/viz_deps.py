import argparse
import requests
from graphviz import Digraph

def strip_version(req):
    req = req.split(';')[0]
    req = req.split('[')[0]
    return req.split('>')[0].split('<')[0].split('=')[0].strip()

def fetch_dependencies(package, max_depth, current_depth=0):
    if current_depth >= max_depth:
        return {}, current_depth

    url = f"https://pypi.org/pypi/{package}/json"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error fetching details for {package}: {response.status_code}")
        return {}, current_depth

    data = response.json()
    dependencies = {}
    requires = data.get('info', {}).get('requires_dist', [])

    if requires:
        req_packages = [strip_version(req) for req in requires]
        dependencies[package] = req_packages
        for dep in req_packages:
            if dep:
                sub_deps, new_depth = fetch_dependencies(dep, max_depth, current_depth + 1)
                dependencies.update(sub_deps)
                current_depth = max(current_depth, new_depth)

    return dependencies, current_depth

def build_graph(dependencies):
    graph = Digraph(comment='Package Dependencies')
    for key, values in dependencies.items():
        for value in values:
            graph.edge(key, value)
    return graph

def visualize_dependencies(program_path, package, output_path, max_depth):
    deps, _ = fetch_dependencies(package, max_depth)
    graph = build_graph(deps)
    graph_path = f"{output_path}/{package}_dep.dot"
    graph.save(graph_path)
    print(f"{program_path} has generated a graph at {graph_path}")

def main():
    parser = argparse.ArgumentParser(description='Visualize Python package dependencies.')
    parser.add_argument('--program_path', required=True, help='Path to the graph visualization program.')
    parser.add_argument('--package', required=True, help='Python package to analyze.')
    parser.add_argument('--output_path', required=True, help='Path to save the graph code output.')
    parser.add_argument('--max_depth', type=int, default=3, help='Maximum depth for dependency analysis.')

    args = parser.parse_args()
    visualize_dependencies(args.program_path, args.package, args.output_path, args.max_depth)

if __name__ == '__main__':
    main()
