from myhdl import *

@block
def hazard_unit(ID_EX_MemRead, ID_EX_RegRt, IF_ID_RegRs,IF_ID_RegRt, Mux_Select_Stall, PCWrite, IF_ID_Write):
    @always_comb
    def HDU():
        if ID_EX_MemRead == 1 and (ID_EX_RegRt == (IF_ID_RegRs or IF_ID_RegRt)):
            Mux_Select_Stall.next = 1
            PCWrite.next = 0
            IF_ID_Write.next = 0
        else:
            Mux_Select_Stall.next = 0
            PCWrite.next = 1
            IF_ID_Write.next = 1
    return HDU
