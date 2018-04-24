from myhdl import block, always_comb


# Always adds 4 to the PC_in
@block
def PC_Increment(PC_in, PC_Plus4):
    @always_comb
    def pc_plus4():
        PC_Plus4.next = PC_in + 4

    return pc_plus4
