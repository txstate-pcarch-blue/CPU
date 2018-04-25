from myhdl import *
from Control import *
from helpers.Clock_Generator import clock_generator
from helpers.Random_Signal import random_signal

if (__name__ == "__main__"):
    #create signal variables
    clk = Signal(intbv(0, 0, 2**1))

    opcode = Signal(intbv(0, 0, 2**6))

    ALUSrc = Signal(intbv(0, 0, 2**1))
    RegDst = Signal(intbv(0, 0, 2**2))
    MemWrite = Signal(intbv(0, 0, 2**1))
    MemRead = Signal(intbv(0, 0, 2**1))
    Beq = Signal(intbv(0, 0, 2**1))
    Jump = Signal(intbv(0, 0, 2**1))
    MemToReg = Signal(intbv(0, 0, 2**2))
    RegWrite = Signal(intbv(0, 0, 2**1))
    ALUOp = Signal(intbv(0, 0, 2**3))
    #create drivers for Signals
    clk_driver = clock_generator(clk)
    op_driver = random_signal(clk, opcode)

    control_driver = traceSignals(control(opcode, ALUSrc, RegDst, MemWrite, MemRead, Beq, Jump, MemToReg, RegWrite, ALUOp))
    #run the simulation
    sim = Simulation(clk_driver, control_driver, op_driver)
    sim.run(1000)
