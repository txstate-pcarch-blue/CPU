from myhdl import *
from IF_ID import if_id
from helpers.Clock_Generator import clock_generator
from helpers.Random_Signal import random_signal
from helpers.Pulse_Generator import pulse_generator

if (__name__ == "__main__"):
    MAX_CYCLES = 1000
    #create signals for variables
    clk = Signal(0)
    inst_in = Signal(intbv(0, 0, 2**32))
    inst_out = Signal(intbv(0, 0, 2**32))
    PC_in = Signal(intbv(0, 0, 2**32))
    PC_out = Signal(intbv(0, 0, 2**32))
    IF_flush = Signal(0)
    IFID_write = Signal(0)
    rst = Signal(0)
    #create drivers for signals
    clock_driver = clock_generator(clk, 10)

    reg_driver = traceSignals(if_id(clk, rst, inst_in, inst_out, PC_in, PC_out, IF_flush, IFID_write))
    inst_driver = random_signal(inst_in, clk)
    PC_driver = random_signal(PC_in, clk)
    IF_flush_driver = pulse_generator(clk, IF_flush, 20)
    IFID_write_driver = pulse_generator(clk, IFID_write)
    #create and run the simulation
    sim = Simulation(clock_driver, reg_driver, inst_driver, PC_driver, IF_flush_driver, IFID_write_driver)
    sim.run(MAX_CYCLES)
