from Registers import *
from Build_Functions import *
from Instructions import *
from collections import namedtuple
import random


# Load configurations from the configuration file infile
# Required keys:
#    i_count = Number of Instructions
#    pf_p = Percentage of instructions for program flow
#    mem_p = Percentage of instructions for lw/sw instructions
#    ALU instructions are generated in the remaining space
def load_config(infile):
    with open(infile, 'r') as f:
        lines = f.readlines()
    conf = namedtuple("conf", ['i_count', 'pf_p', 'mem_p'])
    for line in lines:
        line = line.split('#')[0]  # Remove comments
        if len(line) != 0:
            key, value = line.split(':')
            if key == 'i_count':
                conf.i_count = int(value.strip())
            elif key == 'pf_p':
                conf.pf_p = float(value.strip())
            elif key == 'mem_p':
                conf.mem_p = float(value.strip())
            else:
                print("Invalid config key:", key)
                quit(1)

    return conf


# Generates random ALU instructions in a way that does not change
# registers $0, $sp, $fp, $ra
def generate_alu_instr():
    instr = random.choice(alu_instructions)
    code = instructions[instr]
    if instr in r_instructions:
        rs = rand_register()
        rt = rand_register()
        rd = rand_w_register()
        return build_r(0, rs, rt, rd, 0, code)
    elif instr in i_instructions:
        immediate = random.randint(0, 2**16)
        rs = rand_register()
        rt = rand_w_register()
        return build_i(code, rs, rt, immediate)
    else:  # Error with instruction command
        raise KeyError


# Generates random memory access instructions
def generate_mem_instr():
    instr = random.choice(mem_instructions)
    opcode = i_instructions[instr]
    rs = rand_register()
    rt = rand_w_register()
    immediate = random.randint(0, 2**16)
    return build_i(opcode, rs, rt, immediate)


# Generates valid jump and branch instructions at random
def generate_progflow_instr(labels, max_jump, index):
    instr = random.choice(pf_instructions)
    opcode = instructions[instr]
    if instr == "jr":
        rs = rand_register()
        return build_r(0, rs, 0, 0, 0, opcode)
    elif instr == "beq":
        rs = rand_register()
        rt = rand_register()
        immediate = random.randint(0, max_jump) - index
        if immediate > 128:
            immediate = 128
        elif immediate < -128:
            immediate = -128
        return build_i(opcode, rs, rt, immediate)
    elif instr == "j":
        immediate = random.randint(0, max_jump)
    else:  # instr == "jal"
        immediate = random.choice(list(labels.items()))[1]
    return build_j(opcode, immediate)


# Generates random MIPS instructions in a smart way
#   Creates a python list the size of the intended instruction count
#   Adds 2 functions for jal instructions, then fills in random jump and memory instructions
#   Any instruction still stored as a 0 has not been created and is replaced with random ALU
#     instructions at the end of generation
def generate_code(config):
    instr_list = [0] * config.i_count

    # Ensure the program starts from the beginning if it reaches the end of the file
    instr_list[-1] = build_j(instructions["j"], 0)

    # Build 2 functions 20 instructions long each
    #     Functions can store their stack pointer, but do not have any jumps into or out
    #   beyond the 2 entry / exit points. Filled with only random ALU instructions to prevent
    #   accidental stack overwriting
    #     The first instruction before a function is a jump to 0 to prevent exterior code from entering
    #   the function
    function_template = [0] * 20
    function_template[0] = build_j(instructions["j"], 0)
    # function_template[1] is random ALU Instruction in delay slot
    function_template[2] = parse_i("addi $sp $sp -4", None, 0)
    function_template[3] = parse_i("sw   $ra 0($sp)", None, 0)
    function_template[-4] = parse_i("lw   $ra 0($sp)", None, 0)
    function_template[-3] = parse_i("addi $sp $sp 4", None, 0)
    function_template[-2] = parse_r("jr $ra", None, 0)
    # function_template[-1] is random ALU Instruction in delay slot

    # Store and create function locations
    labels = dict()
    labels['f1'] = len(instr_list) - len(function_template) - 1
    labels['f2'] = len(instr_list) - 2*len(function_template) - 1

    # Add functions to the instruction list
    for i in labels:
        for x, value in enumerate(function_template):
            instr_list[labels[i] + x] = value

    # Generate jump instructions
    for x in range(0, int(config.pf_p * len(instr_list))):
        i = random.randint(0, len(instr_list) - 50)
        if instr_list[i] != 0:
            instr_list[i] = generate_progflow_instr(labels, len(instr_list) - 50, i)

    # Generate mem instructions
    for x in range(0, int(config.mem_p * len(instr_list))):
        i = random.randint(0, len(instr_list) - 50)
        if instr_list[i] != 0:
            instr_list[i] = generate_mem_instr()

    # Fill the empty spaces with random ALU instructions
    for k, v in enumerate(instr_list):
        if v == 0:
            instr_list[k] = generate_alu_instr()
    return instr_list


# Runs as a program if the file is called by python
# This section is ignored if the file is imported instead of called
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="MIPS Code Generator for the blue team CPU")
    parser.add_argument('ofile')
    parser.add_argument('--conf', default="gen.conf", metavar="config_file")
    args = parser.parse_args()
    config = load_config(args.conf)
    generated = generate_code(config)
    normalized = normalize_hex(generated)
    with open(args.ofile, 'w') as f:
        f.writelines(normalized)
