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

        elif opcode == 0x62:
            instructions.append("PUSH3")
            index += 4

        elif opcode == 0x63:
            instructions.append("PUSH4")
            index += 5

        elif opcode == 0x64:
            instructions.append("PUSH5")
            index += 6

        elif opcode == 0x65:
            instructions.append("PUSH6")
            index += 7

        elif opcode == 0x66:
            instructions.append("PUSH7")
            index += 8

        elif opcode == 0x67:
            instructions.append("PUSH8")
            index += 9

        elif opcode == 0x68:
            instructions.append("PUSH9")
            index += 10

        elif opcode == 0x69:
            instructions.append("PUSH10")
            index += 11

        elif opcode == 0x6a:
            instructions.append("PUSH11")
            index += 12

        elif opcode == 0x6b:
            instructions.append("PUSH12")
            index += 13

        elif opcode == 0x6c:
            instructions.append("PUSH13")
            index += 14

        elif opcode == 0x6d:
            instructions.append("PUSH14")
            index += 15

        elif opcode == 0x6e:
            instructions.append("PUSH15")
            index += 16

        elif opcode == 0x6f:
            instructions.append("PUSH16")
            index += 17

        elif opcode == 0x70:
            instructions.append("PUSH17")
            index += 18

        elif opcode == 0x71:
            instructions.append("PUSH18")
            index += 19

        elif opcode == 0x72:
            instructions.append("PUSH19")
            index += 20

        elif opcode == 0x73:
            instructions.append("PUSH20")
            index += 21

        elif opcode == 0x74:
            instructions.append("PUSH21")
            index += 22

        elif opcode == 0x75:
            instructions.append("PUSH22")
            index += 23

        elif opcode == 0x76:
            instructions.append("PUSH23")
            index += 24

        elif opcode == 0x77:
            instructions.append("PUSH24")
            index += 25

        elif opcode == 0x78:
            instructions.append("PUSH25")
            index += 26

        elif opcode == 0x79:
            instructions.append("PUSH26")
            index += 27

        elif opcode == 0x7a:
            instructions.append("PUSH27")
            index += 28

        elif opcode == 0x7b:
            instructions.append("PUSH28")
            index += 29

        elif opcode == 0x7c:
            instructions.append("PUSH29")
            index += 30

        elif opcode == 0x7d:
            instructions.append("PUSH30")
            index += 31

        elif opcode == 0x7e:
            instructions.append("PUSH31")
            index += 32

        elif opcode == 0x7f:
            instructions.append("PUSH32")
            index += 33

        elif opcode == 0x80:
            instructions.append("DUP1")

        elif opcode == 0x81:
            instructions.append("DUP2")

        elif opcode == 0x82:
            instructions.append("DUP3")

        elif opcode == 0x83:
            instructions.append("DUP4")

        elif opcode == 0x84:
            instructions.append("DUP5")

        elif opcode == 0x85:
            instructions.append("DUP6")

        elif opcode == 0x86:
            instructions.append("DUP7")

        elif opcode == 0x87:
            instructions.append("DUP8")

        elif opcode == 0x88:
            instructions.append("DUP9")

        elif opcode == 0x89:
            instructions.append("DUP10")

        elif opcode == 0x8a:
            instructions.append("DUP11")

        elif opcode == 0x8b:
            instructions.append("DUP12")

        elif opcode == 0x8c:
            instructions.append("DUP13")

        elif opcode == 0x8d:
            instructions.append("DUP14")

        elif opcode == 0x8e:
            instructions.append("DUP15")

        elif opcode == 0x8f:
            instructions.append("DUP16")

        elif opcode == 0x90:
            instructions.append("SWAP1")

        elif opcode == 0x91:
            instructions.append("SWAP2")

        elif opcode == 0x92:
            instructions.append("SWAP3")

        elif opcode == 0x93:
            instructions.append("SWAP4")

        elif opcode == 0x94:
            instructions.append("SWAP5")

        elif opcode == 0x95:
            instructions.append("SWAP6")

        elif opcode == 0x96:
            instructions.append("SWAP7")

        elif opcode == 0x97:
            instructions.append("SWAP8")

        elif opcode == 0x98:
            instructions.append("SWAP9")

        elif opcode == 0x99:
            instructions.append("SWAP10")

        elif opcode == 0x9a:
            instructions.append("SWAP11")

        elif opcode == 0x9b:
            instructions.append("SWAP12")

        elif opcode == 0x9c:
            instructions.append("SWAP13")

        elif opcode == 0x9d:
            instructions.append("SWAP14")

        elif opcode == 0x9e:
            instructions.append("SWAP15")

        elif opcode == 0x9f:
            instructions.append("SWAP16")

        elif opcode == 0xa0:
            instructions.append("LOG0")

        elif opcode == 0xa1:
            instructions.append("LOG1")

        elif opcode == 0xa2:
            instructions.append("LOG2")

        elif opcode == 0xa3:
            instructions.append("LOG3")

        elif opcode == 0xa4:
            instructions.append("LOG4")

        elif opcode == 0xf3:
            instructions.append("RETURN")

        elif opcode == 0xf4:
            instructions.append("DELEGATECALL")

        elif opcode == 0xf5:
            instructions.append("CREATE2")

        elif opcode == 0xfa:
            instructions.append("STATICCALL")

        elif opcode == 0xfd:
            instructions.append("REVERT")

        elif opcode == 0xfe:
            instructions.append("INVALID")

        elif opcode == 0xff:
            instructions.append("SELFDESTRUCT")

        else:
            instructions.append("UNKNOWN")

        index += 1

    return instructions

# Example usage
bytecode = b'\x60\x60\x80\xfd\xff'
instructions = disassemble_bytecode(bytecode)
for instruction in instructions:
    print(instruction)
