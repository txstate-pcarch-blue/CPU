from myhdl import *

@block
def isBranch(ALU_zero, Branch, branch_taken):

    @always_comb
    def calc():
        if(ALU_zero and Branch):
            branch_taken.next = 1

    return calc
