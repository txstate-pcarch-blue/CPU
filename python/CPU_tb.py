from myhdl import *
from CPU import CPU
from helpers.Clock_Generator import clock_generator
from helpers.Random_Signal import random_signal

if (__name__ == "__main__"):

    rst = Signal(bool(0))

    regOut = []
    for i in range(0,32):
        regOut.append(Signal(intbv(0, 0, 2**32)))
    CPU_driver = traceSignals(CPU(rst, regOut))

    sim = Simulation(CPU_driver)
    sim.run(200)
