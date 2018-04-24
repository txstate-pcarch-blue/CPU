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
from Hazard_Detection_Unit import hazard_unit
from Multiplexers import *

# Pipeline Registers
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
    IF_ID_instructions = Signal(intbv(0, 0, 2**32))
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
    first_jump_or_branch_mux_2_to_1_out = Signal(intbv(0, 0, 2**32))
    second_jump_or_branch_mux_2_to_1_out = Signal(intbv(0, 0, 2**32))
    third_jump_or_branch_mux_2_to_1_out = Signal(intbv(0, 0, 2**32))
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

    se_driver = Sign_Extender(IF_ID_instructions, immi_sign_extended)

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


    return instances()

