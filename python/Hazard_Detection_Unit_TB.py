from myhdl import *
from Hazard_Detection_Unit import hazard_unit
from helpers.Random_Signal import random_signal
from helpers.Clock_Generator import clock_generator

if (__name__ == "__main__"):
    #inputs
    clk = Signal(intbv(0, 0, 2**1))
    ID_EX_MemRead = Signal(intbv(0, 0, 2**1))
    ID_EX_RegRt = Signal(intbv(0, 0, 2**2))
    IF_ID_RegRs = Signal(intbv(0, 0, 2**2))
    IF_ID_RegRt = Signal(intbv(0, 0, 2**2))
    #outputs
    Mux_Select_Stall= Signal(intbv(0, 0, 2**1))
    PCWrite = Signal(intbv(0, 0, 2**1))
    IF_ID_Write = Signal(intbv(0, 0, 2**1))
    #drivers
    clk_driver = clock_generator(clk)
    ID_EX_MemRead_driver = random_signal(clk, ID_EX_MemRead)
    ID_EX_RegRt_driver = random_signal(clk, ID_EX_RegRt)
    IF_ID_RegRs_driver = random_signal(clk, IF_ID_RegRs)
    IF_ID_RegRt_driver = random_signal(clk, IF_ID_RegRt)

    HDU_driver = traceSignals(hazard_unit(ID_EX_MemRead, ID_EX_RegRt, IF_ID_RegRs, IF_ID_RegRt, Mux_Select_Stall, PCWrite, IF_ID_Write))

    sim = Simulation(clk_driver, ID_EX_MemRead_driver, ID_EX_RegRt_driver, IF_ID_RegRs_driver, IF_ID_RegRt_driver, HDU_driver)
    sim.run(1000)
