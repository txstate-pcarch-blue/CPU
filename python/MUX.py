from myhdl import *

@block
def MUX(ctrl, inputA, inputB, output):

    @always_comb
    def execute():

        if ctrl:
            output.next = inputA
        else:
            output.next = inputB

    return execute
