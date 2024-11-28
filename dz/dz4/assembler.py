import json
import struct
import sys

def assemble(source_file, binary_file, log_file):
    opcode_map = {
        'LOAD_CONST': (7, 'H'),
        'READ_MEM': (1, 'H'),
        'WRITE_MEM': (6, 'I'),
        'DIV': (0, 'I')
    }

    assembled_instructions = []
    with open(source_file, 'r') as file:
        for line in file:
            parts = line.strip().split()
            if not parts or parts[0] not in opcode_map:
                continue
            opcode, fmt = opcode_map[parts[0]]
            operand = int(parts[1])
            instruction = (opcode << 13) | (operand & 0x1FFF)
            if fmt == 'I':
                instruction = struct.pack('>I', (opcode << 29) | (operand & 0x1FFFFFFF))
            else:
                instruction = struct.pack('>H', instruction)
            assembled_instructions.append((parts[0], operand))
            with open(binary_file, 'ab') as bfile:
                bfile.write(instruction)

    with open(log_file, 'w') as logfile:
        json.dump(assembled_instructions, logfile, indent=4)

if __name__ == '__main__':
    _, source_path, binary_path, log_path = sys.argv
    assemble(source_path, binary_path, log_path)
