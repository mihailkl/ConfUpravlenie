import sys
import json
import struct

def execute(binary_file, result_file, memory_range):
    memory = [0] * 3000
    stack = []

    start_range, end_range = map(int, memory_range.split(':'))

    with open(binary_file, 'rb') as file:
        while True:
            header = file.read(1)
            if not header:
                break
            opcode = header[0] >> 5

            if opcode == 7:  # LOAD_CONST
                operand_raw = file.read(1)
                if len(operand_raw) < 1:
                    print("Error: Unexpected end of file.")
                    break
                operand = struct.unpack('>H', header + operand_raw)[0] & 0x1FFF
                stack.append(operand)
            elif opcode == 1:
                if len(stack) < 1:
                    print("Error: Stack is empty on READ_MEM.")
                    break
                operand_raw = file.read(1)
                if len(operand_raw) < 1:
                    print("Error: Unexpected end of file.")
                    break
                operand = struct.unpack('>H', header + operand_raw)[0] & 0x1FFF
                #print(f"!!ПРОБЛЕМА: stack.pop() = {stack.pop()}, operand = {operand}")
                address = stack.pop()
                if start_range <= address <= end_range:
                    stack.append(memory[address])
                    #print(f"on READ_MEM, address = {address}, memory[address] = {memory[address]}")
                else:
                    print(f"Error: Address {address} out of allowed range {start_range} to {end_range}.")
            elif opcode in [0, 6]:  # DIV, WRITE_MEM
                if len(stack) < (1 if opcode == 6 else 2):
                    print(f"Error: Stack is empty on {'DIV' if opcode == 0 else 'WRITE_MEM'}.")
                    break
                operand_raw = file.read(3)
                if len(operand_raw) < 3:
                    print("Error: Insufficient data for operation.")
                    break
                operand = struct.unpack('>I', header + operand_raw)[0] & 0x1FFFFFFF
                if opcode == 0:
                    divisor = memory[operand]
                    dividend = stack.pop()
                    if start_range <= operand <= end_range:
                        result = dividend // divisor
                        stack.append(result)
                        #print(f"dividend = {dividend}, divisor = {divisor}")
                    else:
                        print(f"Error: Division address {operand} out of range.")
                elif opcode == 6:
                    value = stack.pop()
                    address = operand
                    if start_range <= address <= end_range:
                        memory[address] = value
                        #print(f"WRITE_MEM: address = {address}, value = {value}")
                    else:
                        print(f"Error: Address {address} for WRITE out of allowed range {start_range} to {end_range}.")

    result_memory = memory[start_range:end_range + 1]
    with open(result_file, 'w') as file:
        json.dump(result_memory, file, indent=4)

if __name__ == '__main__':
    _, binary_path, result_path, memory_range = sys.argv
    execute(binary_path, result_path, memory_range)