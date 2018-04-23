from myhdl import *

@block
def if_id(clk, rst, inst_in, inst_out, PC_in, PC_out, IF_flush, IFID_write):

    @always(clk.negedge)
    def latch():
        if(rst==1):
            inst_out.next = 0
            PC_out.next = 0
        else:
            if(IF_flush==1):
                inst_out.next = 0
                PC_out.next = 0
            elif(IFID_write==1):
                inst_out.next = inst_in
                PC_out.next = PC_in

    return latch
