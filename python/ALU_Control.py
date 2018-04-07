from myhdl import *

@block
def ALU_Control(clk, op, out): #Clk and OpCode input, int output

    @always(clk.posedge)
    def execute():
        #Insert op code interpretation
        return

    return execute
