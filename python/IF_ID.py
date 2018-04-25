from myhdl import *

@block
def if_id(clk, rst, inst_in, inst_out, PC_in, PC_out, IF_flush, IFID_write):

    @always(clk.posedge)
    def latch():
        #check for reset
        if(rst==1):
            inst_out.next = 0
            PC_out.next = 0
        else:
            #check for flush
            if(IF_flush==1):
                inst_out.next = 0
                PC_out.next = 0
            #if no reset or flush, pass through signals
            elif(IFID_write==1):
                inst_out.next = inst_in
                PC_out.next = PC_in

    return latch
