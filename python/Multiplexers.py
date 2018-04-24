from myhdl import *
#1st ALU source rs:
#Contol is forwarding unit- Forard A
#if 0, selected input is 1st register file's output:rs
#if 1, selected input is forwarded ex to ex
#if 2, selected input is forwarded mem to ex
@block
def first_alu_mux_3_to_1(In1_RegRs, In2_fwdEx, In3_fwdMem, Ctrl_FwdA, out):
    @always_comb
    def mux():
        if Ctrl_FwdA == 0:
            out.next = In1_RegRs
        elif Ctrl_FwdA == 1:
            out.next = In2_fwdEx
        elif Ctrl_FwdA == 2:
            out.next = In3_fwdMem
    return mux

#2nd ALU source rt:
#Control is from Forwarding Unit - Forward B
#if 0, selected input is from 2nd register output rt
#if 1, selected input is forwarded ex to ex
#if 2, selected input is forwarded mem to ex
@block
def second_alu_mux_3_to_1(In1_RegRt, In2_fwdEx, In3_fwdMem, Ctrl_FwdB, out):
    @always_comb
    def mux():
        if Ctrl_FwdB == 0:
            out.next = In1_RegRt
        elif Ctrl_FwdB == 1:
            out.next = In2_fwdEx
        elif Ctrl_FwdB == 2:
            out.next = In3_fwdMem
    return mux

#3rd ALU for source: 2nd mux output feeds into this one
#Control is ALUSrc
#if 0, take input from 2nd mux (can be either 2nd register rt, forwarded mem to ex,
#or forwarded value ex to ex
#if 1, take input from 16 bit immediate after it's sign extended
@block
def third_alu_mux_2_to_1(In1_second_alu_mux, In2_immediate, Ctrl_ALUSrc, out):
    @always_comb
    def mux():
        if Ctrl_ALUSrc == 0:
            out.next = In1_second_alu_mux
        elif Ctrl_ALUSrc == 1:
            out.next = In2_immediate
    return mux

#Mux to determine which destination address will be used to send to ex/mem pipeline stage
#Control: RegDst
#Inputs: rd, rt; Outputs: chosen destiation register
#if 0: rt (immediate type)
#if 1: rd (R type)
@block
def idEx_to_exMem_mux_2_to_1(In1_rd, In2_rt, Ctrl_RegDst, out):
    @always_comb
    def mux():
        if Ctrl_RegDst == 0:
            out.next = In1_rd
        elif Ctrl_RegDst == 1:
            out.next = In2_rt
    return mux

#Mux to determine writeback source (32 bit value)
#Control is MemtoReg
#if 0, R type and take ALU result
#if 1, lw and take mem stage output
#if 2, jal and take hardcoded PC+4 because we need to save in $ra for returning
@block
def writeback_source_mux_3_to_1(In1_ALU_Result, In2_Mem_output, In3_PC_plus_4, Ctrl_MemToReg, out):
    @always_comb
    def mux():
        if Ctrl_MemToReg == 0:
            out.next = In1_ALU_Result
        elif Ctrl_MemToReg == 1:
            out.next = In2_Mem_output
        elif Ctrl_MemToReg == 2:
            out.next = In3_PC_plus_4
    return mux

#Multiplexer reg_dst to determine write address
#Control line is RegDst
#if 0, if some immediate type address comes from 2nd register, bits 20:16
#if 1, R type, address comes from rd, bits 15:11
#if 2, jal and address is hardcoded $31 for $ra slot
@block
def regDst_mux_3_to_1(In1_imm_destination_rt, In2_rType_rd, In3_jal_ra, Ctrl_RegDst, out):
    @always_comb
    def mux():
        if Ctrl_RegDst == 0:
            out.next = In1_imm_destination_rt
        elif Ctrl_RegDst == 1:
            out.next = In2_rType_rd
        elif Ctrl_RegDst == 2:
            out.next = In3_jal_ra
    return mux

#1st Mux: PC + 4 or Branch
#Control lines comes form branch and decision AND gate
#if 0, select PC+4
#if 1, select sign extended label added to PC for BTA
@block
def first_PC4_or_branch_mux_2_to_1(In1_PC_plus_4, In2_BTA, Ctrl_Branch_Gate, out):
    @always_comb
    def mux():
        if Ctrl_Branch_Gate == 0:
            out.next = In1_PC_plus_4
        elif Ctrl_Branch_Gate == 1:
            out.next = In2_BTA
    return mux

#2nd MUX: jump or first mux output
#1st MUX feeds it's output into 2nd as one of the inputs
#2nd input comes from jump_address_calculator
#Control line comes form Control Unit Jump line.
#If 0, it is the 1st input (eitehr PC+4 or BTA depending on 1st MUX reuslt
#If 1, calculated jump address (shift 2, concat top 4 of PC)
@block
def second_jump_or_first_mux_2_to_1(In1_first_mux, In2_jump_addr_calc, Ctrl_Jump, out):
    @always_comb
    def mux():
        if Ctrl_Jump == 0:
            out.next = In1_first_mux
        elif Ctrl_Jump == 1:
            out.next = In2_jump_addr_calc
    return mux

#3rd MUX: jr
#2nd MUX feeds it's output as one of the inputs
#Control line comes form JRControl module in ALU control
#If 0, take 1st input as determined by 2nd MUX
#If 1, we take register value which contains jr address
@block
def third_jr_or_second_mux_2_to_1(In1_second_mux, In2_reg_value_ra, JRCtrl, out):
    @always_comb
    def mux():
        if JRCtrl == 0:
            out.next = In1_second_mux
        elif JRCtrl == 1:
            out.next = In2_reg_value_ra
    return mux

#Hazard detection MUX in ID stage
#2:1 MUX that stalls if lw conflict detected
#Control line; Mux_Select_Stall (from Hazard Until)
#Inputs: Control Unit signal, hardcoded zero
#If 0, output is whatever is send by Control Unit
#If 1, output is 0 and sent to ID/EX wb, m, and ex control lines
@block
def hazard_stall_mux_2_to_1(h_RegWrite, h_MemWrite, Ctrl_Mux_Select_Stall, h_RegWrite_out, h_MemWrite_out):
    @always_comb
    def mux():
        if Ctrl_Mux_Select_Stall == 0:
            h_RegWrite_out.next = h_RegWrite
            h_MemWrite_out.next = h_MemWrite
        elif Ctrl_Mux_Select_Stall == 1:
            h_RegWrite_out.next = 0
            h_MemWrite_out.next = 0
    return mux
