#general purpose 2 to 1 MUX (unused)
from myhdl import *

@block
def MUX(ctrl, inputA, inputB, output):
    @always_comb
    def execute():
        #check which variable to output
        if ctrl:
            output.next = inputA
        else:
            output.next = inputB

    return execute
