import networkx as nx
import matplotlib.pyplot as plt

def disassemble_bytecode(bytecode):
    instructions = []
    index = 0
    length = len(bytecode)
    graph = nx.DiGraph()

    while index < length:
        opcode = bytecode[index]
        instruction = ""

        if opcode < 0x60:
            instruction = f"PUSH{opcode - 0x5f}"
            index += opcode - 0x5e

        elif opcode == 0x60:
            instruction = "PUSH1"
            index += 2

        elif opcode == 0x61:
            instruction = "PUSH2"
            index += 3

        # ... continue handling existing opcodes ...

        elif opcode == 0xfa:
            instruction = "STATICCALL"
            index += 1

        elif opcode == 0xfd:
            instruction = "REVERT"
            index += 1

        elif opcode == 0xfe:
            instruction = "INVALID"
            index += 1

        elif opcode == 0xff:
            instruction = "SELFDESTRUCT"
            index += 1

        else:
            instruction = "UNKNOWN"
            index += 1

        instructions.append(instruction)
        graph.add_edge(instruction, index)

    return instructions, graph

# Example usage
bytecode = b'\x60\x60\x80\xfd\xff'
instructions, graph = disassemble_bytecode(bytecode)

# Print instructions
for instruction in instructions:
    print(instruction)

# Visualize the graph
pos = nx.spring_layout(graph)
nx.draw_networkx(graph, pos, with_labels=True)
plt.show()
