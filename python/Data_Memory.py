from myhdl import *

@block
def Data_Memory(clk, address, write, read, readData, writeData, inmem):
    #modeled inputs and outputs to match model below

    #Use this link's datapath as an example (http://d2vlcm61l7u1fs.cloudfront.net/media%2F63b%2F63b8364b-1ba0-467c-87f2-60b74041b998%2FphpArhSpB.png)
    #Be sure to note that the control line will determine multiplexor
    #that will determine write register(Either writeReg or readA)

    @always(clk.posedge)
    def execute():
        # Insert Memory Read or Write
        if read:
            readData.next = execute.mem[address[10:2]]
        else:
            readData.next = 0
        if write:
            execute.mem[address[10:2]].next = writeData #write register data into memory

    execute.mem = []  #create a mem array with 256 32-bit intbv elements
    for i in range(0, 256):
        execute.mem.append(Signal(intbv(0, 0, 2**32)))

    return execute

