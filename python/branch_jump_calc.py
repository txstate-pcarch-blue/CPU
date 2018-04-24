from myhdl import *

@block
def branch_calculator(In1_extended_imm, In2_pc_plus_4, BTA):

    @always(In1_extended_imm)
    def calc():
        output = intbv(((In1_extended_imm * 4) + In2_pc_plus_4))
        BTA.next = output[32:0]

    return calc

@block
def jump_calculator(In1_instruction, In2_pc_plus_4, Jump_Address):

    @always(In1_instruction)
    def calc():
        temp = intbv((In1_instruction * 4))
        temp[32:28] = In2_pc_plus_4[32:28]
        Jump_Address.next = temp[32:0]

    return calc
