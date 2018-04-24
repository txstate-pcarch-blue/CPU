from myhdl import *

@block
def Instruction_Memory(clk, address, out, infile, mem): #Addr and clk input, out is output

    @always_comb
    def execute():
        # [10:2] is correct, it returns the 8 bits needed for addressing per testing
        #  Do not update to 9:2 unless you are absolutely sure I'm wrong
        out.next = mem[address[10:2]]

    with open(infile) as f:
        for line in f.readlines():
            line = line.strip()
            if line != '':
                mem.append(Signal(intbv((int(line, 16)), 0, 2**32)))

    if len(mem) > 256:
        raise IndexError

    return execute
