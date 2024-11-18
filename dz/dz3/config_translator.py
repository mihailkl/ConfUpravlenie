import sys
import yaml
import argparse

def read_yaml_from_stdin():
    input_data = sys.stdin.read()
    try:
        return yaml.safe_load(input_data)
    except yaml.YAMLError as exc:
        sys.exit(f"Ошибка при чтении YAML: {exc}")

def translate_to_custom_config(data):
    context = {}
    result = []

    for key, value in data.items():
        if isinstance(value, str) and value.startswith("#"):
            value = evaluate_expression(value, context)
        elif isinstance(value, list):
            evaluated_values = [evaluate_expression(v, context) for v in value]
            value = f"array({', '.join(map(str, evaluated_values))})"
        context[key] = value
        result.append(f"global {key} = {value}")

    return "\n".join(result)

def evaluate_expression(expr, context):
    if isinstance(expr, int):
        return expr
    elif isinstance(expr, str):
        if expr.startswith("#["):
            parts = expr[2:-1].strip().split()
            operation = parts[0]
            operands = [evaluate_expression(part, context) for part in parts[1:]]
            if operation == '+':
                return sum(map(int, operands))
            elif operation == 'min':
                return min(map(int, operands))
            elif operation == 'max':
                return max(map(int, operands))
        elif expr.isdigit():
            return int(expr)
        else:
            return context.get(expr, expr)
    return expr


def translate_to_custom_config(data):
    context = {}
    result = []
    
    for key, value in data.items():
        if isinstance(value, str) and value.startswith("#"):
            value = evaluate_expression(value, context)
        elif isinstance(value, list):
            evaluated_values = [evaluate_expression(v, context) for v in value]
            value = f"array({', '.join(map(str, evaluated_values))})"
        context[key] = value
        result.append(f"global {key} = {value}")
    
    return "\n".join(result)

def main():
    parser = argparse.ArgumentParser(description="YAML to Custom Config Translator")
    parser.add_argument("output_file", type=str, help="File path to write the output")
    args = parser.parse_args()
    
    data = read_yaml_from_stdin()
    output = translate_to_custom_config(data)
    
    with open(args.output_file, 'w') as file:
        file.write(output)

if __name__ == "__main__":
    main()