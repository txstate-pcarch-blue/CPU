from helpers.Pulse_Generator import pulse_generator
from myhdl import Signal, Simulation, intbv, traceSignals, instances
from Register_File import RegisterFile
from helpers.Clock_Generator import clock_generator
from helpers.Random_Signal import random_signal

if (__name__ == "__main__"):
    MAX_CYCLES = 100000
    #creates signal variables
    BusA = Signal(intbv(0, 0, 2**32)) #output
    BusB = Signal(intbv(0, 0, 2**32)) #output
    BusW = Signal(intbv(0, 0, 2**32)) #input

    RA = Signal(intbv(0, 0, 2**5)) #input
    RB = Signal(intbv(0, 0, 2**5)) #input
    RW = Signal(intbv(0, 0, 2**5)) #input
    RegWr = Signal(intbv(0, 0, 2**1)) #input
    clk = Signal(intbv(0, 0, 2**1)) #input
    rst = Signal(0) #input
    #makes an array for memory
    outregs = []
    for i in range(0, 32):
        outregs.append(Signal(intbv(0, 0, 2**32)))
        outregs[i].driven = not outregs[i].driven
    #creates drivers for signals
    busWAddress_driver = random_signal(clk, BusW)
    readAAddress_driver = random_signal(clk, RA)
    readBAddress_driver = random_signal(clk, RB)
    readWAddress_driver = random_signal(clk, RW)
    RegWr_driver = pulse_generator(clk, RegWr, delay=2)
    reset_driver = pulse_generator(clk, rst, delay=40)
    register_driver = traceSignals(RegisterFile(BusA, BusB, BusW, RA, RB, RW, RegWr, clk, rst, outregs))
    clock_driver = clock_generator(clk)
    #create and run simulation
    sim = Simulation(instances())
    sim.run(MAX_CYCLES)
