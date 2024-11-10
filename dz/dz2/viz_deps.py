import argparse
import subprocess
import sys
from graphviz import Digraph

def fetch_dependencies(package, max_depth, current_depth=0):
    if current_depth >= max_depth:
        return {}, current_depth
    command = [sys.executable, '-m', 'pip', 'show', package]
    result = subprocess.run(command, capture_output=True, text=True)

    if result.returncode != 0:
        print(f"Error fetching details for {package}: {result.stderr.strip()}")
        return {}, current_depth

    dependencies = {}
    lines = result.stdout.split('\n')
    for line in lines:
        if line.startswith('Requires'):
            _, reqs = line.split(':', 1)
            req_packages = [req.strip() for req in reqs.split(',')]
            dependencies[package] = req_packages
            for dep in req_packages:
                if dep:
                    sub_deps, new_depth = fetch_dependencies(dep, max_depth, current_depth+1)
                    dependencies.update(sub_deps)
                    current_depth = max(current_depth, new_depth)
            break

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
    graph_path = f"{output_path}/{package}_dependencies.dot"
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