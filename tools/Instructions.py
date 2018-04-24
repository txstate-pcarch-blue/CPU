# I-format instructions stored with opcode
i_instructions = {
    "lw": 0x23,
    "sw": 0x2b,
    "addi": 0x08,
    "subi": 0x09,
    "beq": 0x04
}

# J-format instructions stored with opcode
j_instructions = {
    "j": 0x02,
    "jal": 0x03
}

# r-format instructions stored with funct value
r_instructions = {
    "add": 0x20,
    "sub": 0x22,
    "xor": 0x26,
    "jr": 0x08
}

# All instructions, items are using
instructions = dict()

for key in r_instructions:
    instructions[key] = r_instructions[key]
for key in i_instructions:
    instructions[key] = i_instructions[key]
for key in j_instructions:
    instructions[key] = j_instructions[key]

# Program flow instructions
pf_instructions = ["beq", "j", "jr", "jal"]

# Memory management instructions
mem_instructions = ["lw", "sw"]

# ALU operation instructions
alu_instructions = ["add", "sub", "xor", "addi", "subi"]