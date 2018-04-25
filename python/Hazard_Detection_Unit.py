#checks for hazards and stalls when appropriate
from myhdl import *

@block
def hazard_unit(ID_EX_MemRead, ID_EX_RegRt, IF_ID_RegRs,IF_ID_RegRt, Mux_Select_Stall, PCWrite, IF_ID_Write):
    @always_comb
    def HDU():
        #Mux selects which forces control signals for current EX and future MEM_WB to 0 in case of stall
        if ID_EX_MemRead == 1 and (ID_EX_RegRt == (IF_ID_RegRs or IF_ID_RegRt)):
            Mux_Select_Stall.next = 1
            PCWrite.next = 0
            IF_ID_Write.next = 0
        else:
            Mux_Select_Stall.next = 0
            PCWrite.next = 1
            IF_ID_Write.next = 1
    return HDU
#flush IF/ID, ID/EX, and EX/MEM if branch OR jump is determined viable at MEM stage
@block
def branch_or_jump_taken_flush(EX_MEM_branch_out_in, EX_MEM_jump_out_in, EX_MEM_ALU_Zero_out_in, IF_Flush, ID_Flush, EX_Flush, branch_or_jump_taken):

    @always_comb
    def check():
        if((EX_MEM_branch_out_in and EX_MEM_ALU_Zero_out_in) or (EX_MEM_jump_out_in)):
            IF_Flush.next = 1
            ID_Flush.next = 1
            EX_Flush.next = 1
            branch_or_jump_taken.next = 1
        else:
            IF_Flush.next = 0
            ID_Flush.next = 0
            EX_Flush.next = 0
            branch_or_jump_taken.next = 0

    return check
