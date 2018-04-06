from myhdl import *

@block
def Data_Memory(clk, readA, readB, writeReg, writeData, WC, outA, outB):

    #Use this link's datapath as an example (http://d2vlcm61l7u1fs.cloudfront.net/media%2F63b%2F63b8364b-1ba0-467c-87f2-60b74041b998%2FphpArhSpB.png)
    #Be sure to note that the control line will determine multiplexor
    #that will determine write register(Either writeReg or readA)

    @always(clk.posedge)
    def execute():
        #Insert Memory Read or Write

    return execute
