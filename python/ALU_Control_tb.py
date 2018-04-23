from myhdl import *
from helpers.Clock_Generator import clock_generator
from helpers.Random_Signal import random_signal
from ALU_Control import alu_control

if (__name__ == "__main__"):
    clk = Signal(intbv(0, 0, 2**1))
    funct = Signal(intbv(0, 0, 2**6))
    ALUop = Signal(intbv(0, 0, 2**3))
    ALUcontrol = Signal(0)

    clk_driver = clock_generator(clk)
    funct_driver = random_signal(funct, clk)
    ALUop_driver = random_signal(ALUop, clk)
    ALU_driver = traceSignals(alu_control(ALUop, funct, ALUcontrol))

    sim = Simulation(clk_driver, funct_driver, ALUop_driver, ALU_driver)
    sim.run(1000)
