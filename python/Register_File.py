#Use a list of signals to create a homogeneous bit-vector array.

# Logic:
# On HIGH Clock:
#     If the Write Signal is HIGH, Reg[WriteSignal] = Write Data
# Always output the following:
#     Read Data 1 = Registers[Read Addr 1]
#     Read Data 2 = Registers[Read Addr 2]
#
# SP starts at 0xFFFFFFFC

from myhdl import *

@block
def RegisterFile(BusA, BusB, BusW, RA, RB, RW, RegWr, clk, Rst, outregs):

    registers = []
    period = 10


    # Generate Signals of intbv type for registers (Signal is used to track on gtkwave)
    for i in range(0, 32):
        registers.append(Signal(intbv(0, 0, 2**32)))
        registers[i].driven = not registers[i].driven


    #Every posedge of regSig (a.k.a. every quareter clock cycle), perform either read or write (notice write will happen before read)

    @always(delay(10))
    def writeReg():
        nonlocal registers, outregs
        if Rst:
            for i in range(0, 32):
                registers[i].next = Signal(intbv(0, 0, 2**32))
                outregs[i].next = Signal(intbv(0, 0, 2**32))
        elif RegWr and RW != 0:
            registers[RW.unsigned()].next = BusW
            outregs[RW.unsigned()].next = BusW

    @always(clk.negedge)
    def readReg():
        if (Rst):
            BusA.next = Signal(intbv(0, 0, 2**32))
            BusB.next = Signal(intbv(0, 0, 2**32))
        else:
            BusA.next = registers[int(RA)]
            BusB.next = registers[int(RB)]


    '''
    @always(clk.posedge)
    def writeReg():
        nonlocal registers, outregs

        @always(delay(5))
        def deleyReg():
            if Rst:
                for i in range(0, 32):
                    registers[i].next = Signal(intbv(0, 0, 2**32))
                    outregs[i].next = Signal(intbv(0, 0, 2**32))
            elif RegWr and RW != 0:
                registers[RW.unsigned()].next = BusW
                outregs[RW.unsigned()].next = BusW
        return delay

    @always(clk.negedge)
    def readReg():
        nonlocal registers, outregs

        @always(delay(5))
        def delayReg():
            if (Rst):
                BusA.next = Signal(intbv(0, 0, 2**32))
                BusB.next = Signal(intbv(0, 0, 2**32))
            else:
                BusA.next = registers[int(RA)]
                BusB.next = registers[int(RB)]
        return delay
    '''

    return readReg, writeReg
