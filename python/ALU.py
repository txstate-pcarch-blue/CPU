from myhdl import *

@block
def ALU(clk, reset, A, B, CTRL, R, zero): #Note that input and outputs are type intbv type

    @always(clk.posedge)
    def execute():
            #Insert case and arithmetic operation

    return execute #Return for ALU class
