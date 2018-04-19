from myhdl import *

@block
def Sign_Extender(clk, instruction, output):
    #Instruction should be a 16-bit intbv
    #output is accurate 32-bit intbv.
    output.Next = intbv(min = 32, max = 32)
    
    @alway(clk.posedge)
    def execute():
        #Insert 16 to 32-bit conversion loginc
        output[31:16].Next = instruciton[15] #make the first new bits match the first bit
        return output.Next

    return execute
