from myhdl import *

@block
def Instruction_Memory(clk, address, out, infile): #Addr and clk input, out is output

    @always(clk.posedge)
    def execute():
        # [10:2] is correct, it returns the 8 bits needed for addressing per testing
        #  Do not update to 9:2 unless you are absolutely sure I'm wrong
        out.next = execute.mem[address[10:2]]

    execute.mem = []
    with open(infile) as f:
        for line in f.readlines():
            line = line.strip()
            if line != '':
                execute.mem.append(int(line, 16))

    if len(execute.mem) > 256:
        raise IndexError

    return execute
