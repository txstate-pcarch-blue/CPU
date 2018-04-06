from myhdl import *

@block
def Register():

    @alway(clk.posedge)
    def executePos():
        #Insert Write

    @always(clk.negedge)
    def executeNeg():
        #Insert Read
        return

    return executePos, executeNeg
