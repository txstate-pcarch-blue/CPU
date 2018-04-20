from myhdl import *

@block
def Data_Memory(clk, address, read, readData, writeData):
    #modeled inputs and outputs to match model below

    mem = [intbv(max = 2**32)] * 256 #create a mem array with 256 32-bit intbv elements
    
    #Use this link's datapath as an example (http://d2vlcm61l7u1fs.cloudfront.net/media%2F63b%2F63b8364b-1ba0-467c-87f2-60b74041b998%2FphpArhSpB.png)
    #Be sure to note that the control line will determine multiplexor
    #that will determine write register(Either writeReg or readA)

    @always(clk.posedge)
    def execute():
        #Insert Memory Read or Write
        if read == 0: 
            readData.next = mem[address[9:2]] #return memory to be loaded into a register
            return
        elif read == 1:
            mem[address[9:2]] = writeData #write register data into memory
        return

    return execute

