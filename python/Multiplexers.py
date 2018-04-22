from myhdl import *

@block
def first_alu_mux_3_to_1():

    @always_comb
    def mux():
        if(Ctrl_FwdA):

    return mux

@block
def second_alu_mux_3_to_1():

    @always_comb
    def mux():
        if(Ctrl_Fwdb):

    return mux

#Insert other mux here
