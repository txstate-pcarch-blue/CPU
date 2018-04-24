from myhdl import *
from branch_jump_calc import *
from helpers.Clock_Generator import clock_generator
from helpers.Random_Signal import random_signal

if (__name__ == "__main__"):
    clk = Signal(intbv(0, 0, 2**1))
    In1_instruction = Signal(intbv(0, 0, 2**16))
    In2_pc_plus_4 = Signal(intbv(0, 0, 2**32))
    Jump_Address = Signal(intbv(0, 0, 2**32))
    bta_Address = Signal(intbv(0, 0, 2**32))

    clk_driver = clock_generator(clk)
    In1_instruction_driver = random_signal(In1_instruction, clk)
    In2_pc_plus_4_driver = random_signal(In2_pc_plus_4, clk)
    bta = branch_calculator(In1_instruction, In2_pc_plus_4, Jump_Address)
    jump = jump_calculator(In1_instruction, In2_pc_plus_4, bta_Address)
    driver = traceSignals(bta)

    #NOTE: to switch between jump and branch calc just change jump_calculator to branch_calculator
    #then run Simulation

    sim = Simulation(clk_driver, In1_instruction_driver, In2_pc_plus_4_driver, driver)
    sim.run(1000)
