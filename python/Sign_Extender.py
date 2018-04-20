from myhdl import *

@block
def Sign_Extender(clk, instruction, output, out):
    #Instruction should be a 16-bit intbv
    #output is accurate 32-bit intbv.
<<<<<<< HEAD
    output = intbv(max = 2**32)
=======
    output = intbv(min = 0, max = 2**32)
>>>>>>> acd60526204ba20842ea165c2fae01fd91dc48ea
    
    @always(clk.posedge)
    def execute():
        #Insert 16 to 32-bit conversion logic
<<<<<<< HEAD
        for out in output[31:16]:
            output.next = instruction[15] #make the first new bits match the first bit
=======
        for out in output[16:31]:
            out.Next = instruction[15] #make the first new bits match the first bit
>>>>>>> acd60526204ba20842ea165c2fae01fd91dc48ea
        return

    return execute
