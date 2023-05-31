def disassemble_bytecode(bytecode):
    instructions = []
    index = 0
    length = len(bytecode)

    while index < length:
        opcode = bytecode[index]

        if opcode < 0x60:
            instructions.append(f"PUSH{opcode - 0x5f}")
            index += opcode - 0x5e

        elif opcode == 0x60:
            instructions.append("PUSH1")
            index += 2

        elif opcode == 0x61:
            instructions.append("PUSH2")
            index += 3

        # ... continue handling existing opcodes ...

        elif opcode == 0xa5:
            instructions.append("CALLDATALOAD")
            index += 1

        elif opcode == 0xa6:
            instructions.append("CALLDATASIZE")
            index += 1

        elif opcode == 0xa7:
            instructions.append("CALLDATACOPY")
            index += 1

        elif opcode == 0xf6:
            instructions.append("SLOAD")
            index += 1

        elif opcode == 0xf7:
            instructions.append("SSTORE")
            index += 1

        elif opcode == 0xfa:
            instructions.append("STATICCALL")
            index += 1

        elif opcode == 0xfc:
            instructions.append("CREATE")
            index += 1

        elif opcode == 0xfd:
            instructions.append("REVERT")
            index += 1

        elif opcode == 0xfe:
            instructions.append("INVALID")
            index += 1

        elif opcode == 0xff:
            instructions.append("SELFDESTRUCT")
            index += 1

        else:
            instructions.append("UNKNOWN")
            index += 1

    return instructions

# Example usage
bytecode = b'\x60\x60\x80\xfd\xff'
instructions = disassemble_bytecode(bytecode)
for instruction in instructions:
    print(instruction)
