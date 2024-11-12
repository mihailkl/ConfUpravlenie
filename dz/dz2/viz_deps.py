import argparse
import subprocess
import sys
import os

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
            req_packages = [req.strip() for req in reqs.split(',') if req.strip()]
            dependencies[package] = req_packages
            for dep in req_packages:
                sub_deps, new_depth = fetch_dependencies(dep, max_depth, current_depth+1)
                dependencies.update(sub_deps)
                current_depth = max(current_depth, new_depth)
            break

    return dependencies, current_depth

def build_dot_representation(dependencies):
    dot_content = "digraph {\n"
    for key, values in dependencies.items():
        for value in values:
            dot_content += f'    "{key}" -> "{value}"\n'
    dot_content += "}\n"
    return dot_content

def save_dot_file(dot_content, output_path, package):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    graph_path = os.path.join(output_path, f"{package}_dependencies.dot")
    with open(graph_path, 'w') as dot_file:
        dot_file.write(dot_content)
    print(f"The graph has been generated and saved at {graph_path}")

def visualize_dependencies(package, output_path, max_depth):
    deps, _ = fetch_dependencies(package, max_depth)
    dot_content = build_dot_representation(deps)
    save_dot_file(dot_content, output_path, package)

def main():
    parser = argparse.ArgumentParser(description='Visualize Python package dependencies.')
    parser.add_argument('--package', required=True, help='Python package to analyze.')
    parser.add_argument('--output_path', required=True, help='Path to save the graph DOT file.')
    parser.add_argument('--max_depth', type=int, default=3, help='Maximum depth for dependency analysis.')

    args = parser.parse_args()
    visualize_dependencies(args.package, args.output_path, args.max_depth)

if __name__ == '__main__':
    main()
