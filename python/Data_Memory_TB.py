from myhdl import Signal, Simulation, intbv, traceSignals
from Data_Memory import Data_Memory
from Clock_Generator import clock_generator
from Random_Signal import random_signal
  
# Program Counter Testbench
# Runs the PC for max_cycles
# Gives the branch signal and a new address every 10 cycles
if (__name__ == "__main__"):
    MAX_CYCLES = 1000

    address = Signal(intbv(0, 0, 2**32))
    read = Signal(0)
    writeData = Signal(intbv(0, 0, 2**32))
    readData = Signal(intbv(0, 0, 2**32))
    output = Signal(intbv(0, 0, 2**32))
    clk = Signal(0)

    data_driver = traceSignals(Data_Memory(clk, address, read, readData, writeData))
    clock_driver = clock_generator(clk)
    rand_driver  = random_signal(address, clk)
  
    sim = Simulation(clock_driver, rand_driver, data_driver)
    sim.run(MAX_CYCLES)
