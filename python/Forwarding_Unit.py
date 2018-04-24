from myhdl import *


@block
def ForwardingUnit(ID_EX_RegRs, ID_EX_RegRt, EX_MEM_RegRd, EX_MEM_RegWrite, MEM_WB_RegRd, MEM_WB_RegWrite, Mux_ForwardA, Mux_ForwardB):

    @always_comb
    def forwarding_unit():
        if (EX_MEM_RegWrite == 1 and EX_MEM_RegRd == ID_EX_RegRs):
            Mux_ForwardA.next = 2
        if (EX_MEM_RegWrite == 1 and EX_MEM_RegRd == ID_EX_RegRt):
            Mux_ForwardB.next = 2
        if (MEM_WB_RegWrite == 1 and MEM_WB_RegRd == ID_EX_RegRs and (EX_MEM_RegRd != ID_EX_RegRs or EX_MEM_RegWrite == 0)):
            Mux_ForwardA.next = 1
        if (MEM_WB_RegWrite == 1 and MEM_WB_RegRd == ID_EX_RegRt and (EX_MEM_RegRd != ID_EX_RegRt or EX_MEM_RegWrite == 0)):
            Mux_ForwardB.next = 1

    return forwarding_unit
