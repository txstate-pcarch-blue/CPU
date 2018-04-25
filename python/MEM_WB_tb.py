from myhdl import *
from MEM_WB import mem_wb
from helpers.Clock_Generator import clock_generator
from helpers.Random_Signal import random_signal
from helpers.Pulse_Generator import pulse_generator

if (__name__ == "__main__"):
    MAX_CYCLES = 1000
    #create signal variables
    clk = Signal(0)
    RegWrite_in = Signal(0)
    MemtoReg_in = Signal(intbv(0, 0, 2**2))
    D_MEM_read_data_in = Signal(intbv(0, 0, 2**32))
    D_MEM_read_addr_in = Signal(intbv(0, 0, 2**32))
    EX_MEM_RegisterRd_in = Signal(intbv(0, 0, 2**5))
    D_MEM_read_data_out = Signal(intbv(0, 0, 2**32))
    D_MEM_read_addr_out = Signal(intbv(0, 0, 2**32))
    MEM_WB_RegisterRd_out = Signal(intbv(0, 0, 2**5))
    RegWrite_out = Signal(0)
    MemtoReg_out = Signal(intbv(0, 0, 2**2))

    rst = Signal(0)
    #create drivers for variables
    clock_driver = clock_generator(clk, 10)

    reg_driver = traceSignals(mem_wb(clk, rst, RegWrite_in, MemtoReg_in, D_MEM_read_data_in, D_MEM_read_addr_in,
                                    EX_MEM_RegisterRd_in, D_MEM_read_data_out, D_MEM_read_addr_out, MEM_WB_RegisterRd_out,
                                    RegWrite_out, MemtoReg_out))
    MemtoReg_in_driver = random_signal(MemtoReg_in, clk)
    D_MEM_read_data_in_driver = random_signal(D_MEM_read_data_in, clk)
    D_MEM_read_addr_in_driver = random_signal(D_MEM_read_addr_in, clk)
    EX_MEM_RegisterRd_in_driver = random_signal(EX_MEM_RegisterRd_in, clk)
    RegWrite_in_driver = pulse_generator(clk, RegWrite_in, 20)
    #create and run the simulation
    sim = Simulation(clock_driver, reg_driver, MemtoReg_in_driver,
                        D_MEM_read_data_in_driver, D_MEM_read_addr_in_driver, EX_MEM_RegisterRd_in_driver,
                        RegWrite_in_driver)
    sim.run(MAX_CYCLES)
