from myhdl import *

@block
def isBranch(ALU_zero, Branch, branch_taken):
    #check to see if a branch is being taken and report signal
    @always_comb
    def calc():
        if(ALU_zero and Branch):
            branch_taken.next = 1

    return calc
