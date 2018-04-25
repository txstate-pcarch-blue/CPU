from myhdl import *

@block
def if_id(clk, rst, inst_in, inst_out, PC_in, PC_out, IF_flush, IFID_write):
    '''
    class latches:
        inst_in = Signal(0)
        PC_in = Signal(0)
        inst_out = Signal(intbv(0))
        PC_out = Signal(intbv(0))

    '''
    @always(clk.posedge)
    def read():
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
    '''
    @always(delay(10))
    def read():
        inst_out.next = latches.inst_in
        PC_out.next = latches.PC_in

    @always(clk.negedge)
    def write():
        if(IF_flush==1):
            latches.inst_in = intbv(0)
            latches.PC_out = intbv(0)
        elif(IFID_write==1):
            latches.inst_out = inst_in
            latches.PC_out = PC_in
            '''
    return read
