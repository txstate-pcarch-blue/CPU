from myhdl import *
from ID_EX import id_ex
from helpers.Clock_Generator import clock_generator
from helpers.Random_Signal import random_signal

if (__name__ == "__main__"):
    MAX_CYCLES = 1000

    readA_out = Signal(intbv(0, 0, 2**32))
    readB_out = Signal(intbv(0, 0, 2**32))
    offset_out = Signal(intbv(0, 0, 2**32))
    PC_Plus4_out = Signal(intbv(0, 0, 2 ** 32))
    branch_out = Signal(intbv(0, 0, 2**1))
    branch_addr_out = Signal(intbv(0, 0, 2**32))
    RT_out = Signal(intbv(0, 0, 2**5))
    RS_out = Signal(intbv(0, 0, 2**5))
    RD_out = Signal(intbv(0, 0, 2**5))
    WB_out = Signal(intbv(0, 0, 2**1))
    RegWrite_out = Signal(intbv(0, 0, 2**1))
    ALUSrc_out = Signal(intbv(0, 0, 2**1))
    ALUOp_out = Signal(intbv(0, 0, 2**2))
    RegDst_out = Signal(intbv(0, 0, 2**2))
    Jump_out = Signal(intbv(0, 0, 2**1))
    jump_addr_out = Signal(intbv(0, 0, 2**32))
    immi_sign_extended_out = Signal(intbv(0, 0, 2**32))
    MemToReg_out = Signal(intbv(0, 0, 2**1))
    MemWrite_out = Signal(intbv(0, 0, 2**1))
    MemRead_out = Signal(intbv(0, 0, 2**1))
    lwFlush_out = Signal(intbv(0, 0, 2**1))
    brFlush_out = Signal(intbv(0, 0, 2**1))
    funct_out = Signal(intbv(0, 0, 2**6))
    opCode_out = Signal(intbv(0, 0, 2**3))

    readA_in = Signal(intbv(0, 0, 2**32))
    readB_in = Signal(intbv(0, 0, 2**32))
    branch_in = Signal(intbv(0, 0, 2**1))
    offset_in = Signal(intbv(0, 0, 2**32))
    branch_addr_in = Signal(intbv(0, 0, 2**32))
    jump_addr_in = Signal(intbv(0, 0, 2**32))
    immi_sign_extended_in = Signal(intbv(0, 0, 2**32))
    PC_Plus4_in = Signal(intbv(0, 0, 2 ** 32))
    RT_in = Signal(intbv(0, 0, 2**5))
    RS_in = Signal(intbv(0, 0, 2**5))
    RD_in = Signal(intbv(0, 0, 2**5))
    WB_in = Signal(intbv(0, 0, 2**1))
    MemToReg_in = Signal(intbv(0, 0, 2**1))
    MemWrite_in = Signal(intbv(0, 0, 2**1))
    MemRead_in = Signal(intbv(0, 0, 2**1))
    Jump_in = Signal(intbv(0, 0, 2**1))
    RegWrite_in = Signal(intbv(0, 0, 2**1))
    ALUSrc_in = Signal(intbv(0, 0, 2**1))
    ALUOp_in = Signal(intbv(0, 0, 2**2))
    RegDst_in = Signal(intbv(0, 0, 2**2))
    lwFlush_in = Signal(intbv(0, 0, 2**1))
    brFlush_in = Signal(intbv(0, 0, 2**1))
    funct_in = Signal(intbv(0, 0, 2**6))
    opCode_in = Signal(intbv(0, 0, 2**3))

    clock = Signal(0)
    reset = Signal(0)
    ID_Hazard_lwstall = Signal(intbv(0, 0, 2**1))
    ID_Hazard_branch = Signal(intbv(0, 0, 2**1))

    reg_driver = traceSignals(id_ex(clock, reset, ID_Hazard_lwstall, ID_Hazard_branch, branch_in,
                                    MemRead_in, MemWrite_in, Jump_in, RegWrite_in, ALUSrc_in, ALUOp_in,
                                    RegDst_in, MemToReg_in, jump_addr_in, PC_Plus4_in, branch_addr_in,
                                    readA_in, readB_in, immi_sign_extended_in, RS_in, RT_in, RD_in,
                                    funct_in, RegWrite_out, branch_out, MemRead_out, MemWrite_out,
                                    Jump_out, ALUSrc_out, ALUOp_out, RegDst_out, MemToReg_out, jump_addr_out, PC_Plus4_out,
                                    branch_addr_out, readA_out, readB_out, immi_sign_extended_out, RS_out, RT_out,
                                    RD_out, funct_out))

    clock_driver = clock_generator(clock)

    ID_Hazard_b_driver = random_signal(clock, ID_Hazard_branch)
    ID_Hazard_lw_driver = random_signal(clock, ID_Hazard_lwstall)
    branch_in_driver = random_signal(clock, branch_in)
    MemRead_driver = random_signal(clock, MemRead_in)
    MemWrite_driver = random_signal(clock, MemWrite_in)
    Jump_driver = random_signal(clock, Jump_in)
    RegWrite_driver = random_signal(clock, RegWrite_in)
    ALUSrc_driver = random_signal(clock, ALUSrc_in)
    ALUOp_driver = random_signal(clock, ALUOp_in)
    RegDst_driver = random_signal(clock, RegDst_in)
    MemToReg_driver = random_signal(clock, MemToReg_in)
    jump_addr_driver = random_signal(clock, jump_addr_in)
    PC_Plus4_driver = random_signal(clock, PC_Plus4_in)
    branch_addr_driver = random_signal(clock, branch_addr_in)
    readA_driver = random_signal(clock, readA_in)
    readB_driver = random_signal(clock, readB_in)
    immi_sign_extended_driver = random_signal(clock, immi_sign_extended_in)
    RT_driver = random_signal(clock, RT_in)
    RS_driver = random_signal(clock, RS_in)
    RD_driver = random_signal(clock, RD_in)
    funct_driver = random_signal(clock, funct_in)

    sim = Simulation(instances())
    sim.run(MAX_CYCLES)
