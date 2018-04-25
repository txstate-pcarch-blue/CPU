#testbench for all 10 multiplexers
#used comments to prevent from running all at once, gtkwave didn't like it
from myhdl import *
from Multiplexers import *
from helpers.Pulse_Generator import pulse_generator
from helpers.Random_Signal import random_signal
from helpers.Clock_Generator import clock_generator

if (__name__ == "__main__"):
    #create signal variables
    clk = Signal(intbv(0, 0 , 2**1))
    ctrl = Signal(intbv(0, 0, 2**2))
    input1 = Signal(intbv(0, 0, 2**32))
    input2 = Signal(intbv(0, 0, 2**32))
    input3 = Signal(intbv(0, 0, 2**32))
    output = Signal(intbv(0, 0, 2**32))
    #create drivers for signals
    clk_driver = clock_generator(clk)
    ctrl_driver = random_signal(ctrl, clk)
    input1_driver = random_signal(input1, clk)
    input2_driver = random_signal(input2, clk)
    input3_driver = random_signal(input3, clk)
    #instances to try and run all multiplexers at once
    def instances():
        #MUX1_driver = traceSignals(first_alu_mux_3_to_1(input1, input2, input3, ctrl, output))
        #MUX2_driver = traceSignals(second_alu_mux_3_to_1(input1, input2, input3, ctrl, output))
        #MUX3_driver = traceSignals(third_alu_mux_2_to_1(input1, input2, ctrl, output))
        #MUX4_driver = traceSignals(idEx_to_exMem_mux_2_to_1(input1, input2, ctrl, output))
        #MUX5_driver = traceSignals(writeback_source_mux_3_to_1(input1, input2, input3, ctrl, output))
        #MUX6_driver = traceSignals(regDst_mux_3_to_1(input1, input2, input3, ctrl, output))
        #MUX7_driver = traceSignals(first_jump_or_branch_mux_2_to_1(input1, input2, ctrl, output))
        #MUX8_driver = traceSignals(second_jump_or_branch_mux_2_to_1(input1, input2, ctrl, output))
        #MUX9_driver = traceSignals(third_jump_or_branch_mux_2_to_1(input1, input2, ctrl, output))
        MUXX_driver = traceSignals(hazard_stall_mux_2_to_1(input1, input2, ctrl, output))
        return clk_driver, ctrl_driver, input1_driver, input2_driver, input3_driver, MUXX_driver
    #create and run simulation
    sim = Simulation(instances())
    sim.run(1000)
