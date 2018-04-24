from myhdl import *

@block
def Sign_Extender(instruction, output):
    #Instruction should be a 16-bit intbv
    #output is accurate 32-bit intbv.
    @always_comb
    def execute():
        out = intbv(0, 0, 2**32)
        #Insert 16 to 32-bit conversion logic
        for i in range(0, 16):
            out[i] = instruction[i]
        for i in range(16, 32):
            out[i] = instruction[15] #make the first new bits match the first bit
        output.next = out

    return execute
