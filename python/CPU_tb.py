from myhdl import *
from CPU import CPU
from helpers.Clock_Generator import clock_generator
from helpers.Random_Signal import random_signal

if (__name__ == "__main__"):

    clk = Signal(0)
    rst = Signal(0)

    clk_driver = clock_generator(clk)
    CPU_driver = traceSignals(CPU(clk, rst))

    sim = Simulation(clk_driver, CPU_driver)
    sim.run(1000)
