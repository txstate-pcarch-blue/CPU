# Type imports
from myhdl import intbv, Signal, always, block, instances

# Module Imports
from PC import program_counter
from Instruction_Memory import Instruction_Memory
from Register_File import RegisterFile
from ALU import alu
from Data_Memory import Data_Memory
from Sign_Extender import Sign_Extender

# Control Imports
from Control import Control
from ALU_Control import alu_control
from branch_jump_calc import branch_calculator
from Forwarding_Unit import ForwardingUnit
from Hazard_Detection_Unit import *
from Multiplexers import *

# Pipeline Registers Imports
from IF_ID import if_id
from ID_EX import id_ex
from EX_MEM import ex_mem
from MEM_WB import mem_wb

# CPU Assignments
from CPU_Assigns import *

# CPU - five stage MIPS CPU with forwarding and hazard control
# This file drives the processor. Control wiring signals are handled here.
# Wires are associated with their respective stage
# Multiplexers drive control decision making
# Modules receive pre-determined inputs based on mux output
@block
def CPU(clock, reset, registers):
    # Wires in the IF stage
    PC_out = Signal(intbv(0, 0, 2**32))
    PC_plus4 = Signal(intbv(0, 0, 2**32))
    instruction_out = Signal(intbv(0, 0, 2**32))
    PO_write = Signal(intbv(0, 0, 2**1))

    # PC_Plus4 assignment
    pcp4_driver = PC_Increment(PC_out, PC_plus4)

    # Wires in the ID stage
    IF_ID_PC_plus4 = Signal(intbv(0, 0, 2**32))
    IF_ID_instruction = Signal(intbv(0, 0, 2**32))
    MEM_WB_RegisterRd = Signal(intbv(0, 0, 2**4))
    reg_read_data_1 = Signal(intbv(0, 0, 2**32))
    reg_read_data_2 = Signal(intbv(0, 0, 2**32))
    immi_sign_extended = Signal(intbv(0, 0, 2**32))

    # Jump within the ID stage
    BTA = Signal(intbv(0, 0, 2**32))
    Jump_Address = Signal(intbv(0, 0, 2**32))
    jump_base28 = Signal(intbv(0, 0, 2**28))

    # Control Signal generation within the ID stage
    Jump = Signal(0)
    Branch = Signal(0)
    MemRead = Signal(0)
    MemWrite = Signal(0)
    ALUSrc = Signal(0)
    RegWrite = Signal(0)
    RegDst = Signal(intbv(0, 0, 2**2))
    MemToReg = Signal(intbv(0, 0, 2**2))
    ALUop = Signal(intbv(0, 0, 2**3))

    # ID Stage constants
    In3_jal_ra = Signal(intbv(31, 0, 2**5))

    # Mux output wires
    first_alu_mux_3_to_1_out = Signal(intbv(0, 0, 2**32))
    second_alu_mux_3_to_1_out = Signal(intbv(0, 0, 2**32))
    third_alu_mux_2_to_1_out = Signal(intbv(0, 0, 2**32))
    idEx_to_exMem_mux_2_to_1_out = Signal(intbv(0, 0, 2**5))
    writeback_source_mux_3_to_1_out = Signal(intbv(0, 0, 2**32))
    regDst_mux_3_to_1_out = Signal(intbv(0, 0, 2**5))
    first_PC4_or_branch_mux_2_to_1_out = Signal(intbv(0, 0, 2**32))
    second_jump_or_first_mux_2_to_1_out = Signal(intbv(0, 0, 2**32))
    third_jr_or_second_mux_2_to_1_out = Signal(intbv(0, 0, 2**32))
    h_RegWrite_out = Signal(0)
    h_MemWrite_out = Signal(0)

    # Wires for the LW hazard stall
    PCWrite = Signal(0)            # PC stop writing if PCWrite == 0
    IF_ID_Write = Signal(0)        # IF/ID reg stops writing if IF_ID_Write == 0
    ID_Flush_lwstall = Signal(0)

    # Wires for jump/branch control
    PCSrc = Signal(0)
    IF_Flush = Signal(0)
    ID_Flush_Branch = Signal(0)
    EX_Flush = Signal(0)

    # Register wires
    regOut = []
    for i in range(0, 32):
        regOut.append(Signal(intbv(0, 0, 2**32)))

    se_driver = Sign_Extender(IF_ID_instruction, immi_sign_extended)

    # Wires in the EX stage
    ID_EX_Jump = Signal(0)
    ID_EX_Branch = Signal(0)
    ID_EX_MemRead = Signal(0)
    ID_EX_MemWrite = Signal(0)
    ID_EX_ALUSrc = Signal(0)
    ID_EX_RegWrite = Signal(0)
    ALU_zero = Signal(0)
    JRControl = Signal(0)
    ID_EX_jump_addr = Signal(intbv(0, 0, 2**32))
    ID_EX_branch_addr = Signal(intbv(0, 0, 2**32))
    ID_EX_PC_plus4 = Signal(intbv(0, 0, 2**32))
    ID_EX_reg_read_data_1 = Signal(intbv(0, 0, 2**32))
    ID_EX_reg_read_data_2 = Signal(intbv(0, 0, 2**32))
    ID_EX_immi_sign_extended = Signal(intbv(0, 0, 2**32))
    muxA_out = Signal(intbv(0, 0, 2**32))
    muxB_out = Signal(intbv(0, 0, 2**32))
    after_ALUSrc = Signal(intbv(0, 0, 2**32))
    ALU_result = Signal(intbv(0, 0, 2**32))
    after_shift = Signal(intbv(0, 0, 2**32))
    ID_EX_RegDst = Signal(intbv(0, 0, 2**2))
    ID_EX_MemtoReg = Signal(intbv(0, 0, 2**2))
    out_to_ALU = Signal(intbv(0, 0, 2**2))
    ID_EX_ALUOp = Signal(intbv(0, 0, 2**3))
    ID_EX_RegisterRs = Signal(intbv(0, 0, 2**5))
    ID_EX_RegisterRt = Signal(intbv(0, 0, 2**5))
    ID_EX_RegisterRd = Signal(intbv(0, 0, 2**5))
    EX_RegisterRd = Signal(intbv(0, 0, 2**5))
    ID_EX_funct = Signal(intbv(0, 0, 2**6))

    # Wires in the MEM stage
    EX_MEM_RegisterRd = Signal(intbv(0, 0, 2**5))
    EX_MEM_Branch = Signal(0)
    EX_MEM_MemRead = Signal(0)
    EX_MEM_MemWrite = Signal(0)
    EX_MEM_Jump = Signal(0)
    Branch_taken = Signal(0)
    EX_MEM_ALU_zero = Signal(0)
    EX_MEM_MemtoReg = Signal(intbv(0, 0, 2**2))
    EX_MEM_jump_addr = Signal(intbv(0, 0, 2**32))
    EX_MEM_branch_addr = Signal(intbv(0, 0, 2**32))
    EX_MEM_ALU_result = Signal(intbv(0, 0, 2**32))
    EX_MEM_reg_read_data_2 = Signal(intbv(0, 0, 2**32))
    D_MEM_data = Signal(intbv(0, 0, 2**32))

    # Wires in the WB Stage
    reg_write_data = Signal(intbv(0, 0, 2**32))
    MEM_WB_RegWrite = Signal(0)
    MEM_WB_MemtoReg = Signal(intbv(0, 0, 2**2))
    MEM_WB_D_MEM_read_data = Signal(intbv(0, 0, 2**32))
    MEM_WB_D_MEM_read_addr = Signal(intbv(0, 0, 2**32))

    # Wires for forwarding
    ForwardA = Signal(intbv(0, 0, 2**2))
    ForwardB = Signal(intbv(0, 0, 2**2))

    #IF stage: PC, IM, IF_ID_Reg
    Unit0 = program_counter(clock, reset, PC_out, third_alu_mux_2_to_1_out, PCWrite)
    Unit1 = Instruction_Memory(clock, PC_out, instruction_out, "instructions.txt") # TODO: infile #)
    Unit3 = if_id(clock, reset, instruction_out, IF_ID_instruction, PC_plus4, IF_ID_PC_plus4, IF_Flush, IF_ID_Write)

    #ID Stage: Control, Registers, branch_jump_cal, sign_extend, regDst_mux_3_to_1,
    #ID_EX_reg, Hazard_Detection_Unit
    Unit4 = Control(IF_ID_instruction[32:26], ALUSrc, RegDst, MemWrite, MemRead, Branch, Jump, MemToReg, RegWrite, ALUOp)
    Unit5 = regDst_mux_3_to_1(IF_ID_instruction[21:16], IF_ID_instruction[26:21], In3_jal_ra, RegDst, regDst_mux_3_to_1_out)
    Unit25 = hazard_unit(ID_EX_MemRead, ID_EX_RegisterRt, IF_ID_instruction[26:21], IF_ID_instruction[21:16], ID_Flush_lwstall, PCWrite, IF_ID_Write)
    Unit6 = hazard_stall_mux_2_to_1(RegWrite, MemWrite, ID_Flush_lwstall, h_RegWrite_out, h_MemWrite_out)
    Unit7 = RegisterFile(reg_read_data_1, reg_read_data_2, reg_write_data, IF_ID_instruction[26:21], IF_ID_instruction[21:16], regDst_mux_3_to_1_out, RegWrite, clock, reset, regOut)
    Unit8 = branch_calculator(immi_sign_extended, IF_ID_PC_plus4, BTA)
    Unit9 = jump_calculator(IF_ID_instruction, IF_ID_PC_plus4, Jump_Address)
    Unit24 = id_ex(clock, reset, ID_Flush_lwstall, ID_Flush_Branch, Branch, MemRead, MemWrite, Jump, RegWrite, ALUSrc, ALUOp, RegDst, MemToReg, Jump_Address, BTA, IF_ID_PC_plus4, reg_read_data_1, reg_read_data_2, IF_ID_instruction[26:21], IF_ID_instruction[21:16], IF_ID_instruction[16:11], IF_ID_instruction[6:0], ID_EX_RegWrite, ID_EX_Branch, ID_EX_MemRead, ID_EX_MemWrite, ID_EX_Jump, ID_EX_ALUSrc, ID_EX_ALUOp, ID_EX_RegDst, ID_EX_MemtoReg, ID_EX_jump_addr, ID_EX_branch_address, ID_EX_PC_plus4, ID_EX_reg_read_data_1, ID_EX_reg_read_data_2, ID_EX_immi_sign_extended, ID_EX_RegisterRs, ID_EX_RegisterRt, ID_EX_RegisterRd, ID_EX_funct)

    #EX Stage:
    Unit11 = alu_control(ID_EX_ALUOp, ID_EX_funct, out_to_ALU)
    Unit12 = JR_Control(ID_EX_ALUOp, ID_EX_funct, JRControl)
    #ID_EX_RegRs, ID_EX_RegRt, EX_MEM_RegRd, EX_MEM_RegWrite, MEM_WB_RegRd, MEM_WB_RegWrite, Mux_ForwardA, Mux_ForwardB
    Unit13 = ForwardingUnit(ID_EX_RegisterRs, ID_EX_RegisterRt, EX_MEM_RegisterRd, EX_MEM_RegWrite, ) #TODO: Finish ForwardingUnit on both python and Verilog
    Unit14 = first_alu_mux_3_to_1(ID_EX_reg_read_data_1, EX_MEM_reg_read_data_2, MEM_WB_D_MEM_read_data, ForwardA, first_alu_mux_3_to_1_out)
    Unit15 = second_alu_mux_3_to_1(ID_EX_reg_read_data_2, EX_MEM_reg_read_data_2, MEM_WB_D_MEM_read_data, ForwardB, second_alu_mux_3_to_1_out)
    Unit16 = third_alu_mux_2_to_1(second_alu_mux_3_to_1_out, immi_sign_extended, ALUSrc, third_alu_mux_2_to_1_out)
    clk, reset, A, B, CTRL, R, zero
    Unit10 = alu(clock, reset, first_alu_mux_3_to_1_out, third_alu_mux_2_to_1_out, out_to_ALU, ALU_result, ALU_zero)
    Unit17 = idEx_to_exMem_mux_2_to_1(ID_EX_RegisterRd, ID_EX_RegisterRt, ID_EX_RegDst, idEx_to_exMem_mux_2_to_1_out)
    Unit18 = ex_mem(clock, reset, EX_Flush, ID_EX_RegWrite, ID_EX_MemtoReg, ID_EX_Branch, ID_EX_MemRead, ID_EX_MemWrite, ID_EX_Jump, ID_EX_jump_addr, ID_EX_branch_address, ALU_zero, ALU_result, second_alu_mux_3_to_1_out, idEx_to_exMem_mux_2_to_1_out, EX_MEM_RegWrite, EX_MEM_MemtoReg, EX_MEM_Branch, EX_MEM_MemRead, EX_MEM_MemWrite, EX_MEM_Jump, EX_MEM_jump_addr, EX_MEM_branch_addr, EX_MEM_ALU_zero, EX_MEM_ALU_result, EX_MEM_reg_read_data_2, EX_MEM_RegisterRd)

    #Mem Stage:
    unit26 = branch_or_jump_taken_flush(EX_MEM_Branch, EX_MEM_Jump, EX_MEM_ALU_zero, IF_Flush, ID_Flush_Branch, EX_Flush)

    return instances()
