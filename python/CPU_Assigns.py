from myhdl import *


# Always adds 4 to the PC_in
@block
def PC_Increment(clk, PC_in, PC_Plus4):

    @always(clk.posedge)
    def pc_plus4():
        PC_Plus4.next = intbv(PC_in + 4)

    return pc_plus4
