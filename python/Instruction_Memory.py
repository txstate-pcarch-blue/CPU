from myhdl import *

@block
def Instruction_Memory(clk, address, out): #Addr and clk input, out is output
    
    mem = [intbv(max = 2**32)] * 256 #create 256 32-bit memory array

    @always(clk.posedge)
    def execute():
        out.next = mem[address[9:2]] #return the address of the instruciton
        return

    return execute
