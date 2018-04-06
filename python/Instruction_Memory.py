from myhdl import *

@block
def Instruction_Memory(clk, Addr, Out): #Addr and clk input, out is output

    @always(clk.posedge)
    def execute:

    return execute
