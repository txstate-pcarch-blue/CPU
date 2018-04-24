#EX_MEM Pipeline Register

from myhdl import *

@block
def ex_mem(clk, rst, EX_Flush, RegWrite_in, MemtoReg_in, Branch_in, MemRead_in,
            MemWrite_in, Jump_in, jump_addr_in, branch_addr_in, ALU_zero_in,
            ALU_result_in, reg_read_data_2_in, ID_EX_RegisterRd_in, PC_plus_4_in, RegWrite_out,
            MemtoReg_out, Branch_out, MemRead_out, MemWrite_out, Jump_out,
            jump_addr_out, branch_addr_out, ALU_zero_out, ALU_result_out,
            reg_read_data_2_out, EX_MEM_RegisterRd_out, PC_plus_4_out):

    @always(clk.posedge)
    def latches():
        if(rst==1):
            RegWrite_out.next = 0
            MemtoReg_out.next = 0
            Branch_out.next = 0
            MemRead_out.next = 0
            MemWrite_out.next = 0
            Jump_out.next = 0
            jump_addr_out.next = 0
            branch_addr_out.next = 0
            ALU_zero_out.next = 0
            ALU_result_out.next = 0
            reg_read_data_2_out.next = 0
            EX_MEM_RegisterRd_out.next = 0
            PC_plus_4_out.next = 0
        else:
            RegWrite_out.next = RegWrite_in
            MemtoReg_out.next = MemtoReg_in
            Branch_out.next = Branch_in
            MemRead_out.next = MemRead_in
            MemWrite_out.next = MemWrite_in
            Jump_out.next = Jump_in
            jump_addr_out.next = jump_addr_in
            branch_addr_out.next = branch_addr_in
            ALU_zero_out.next = ALU_zero_in
            ALU_result_out.next = ALU_result_in
            reg_read_data_2_out.next = reg_read_data_2_in
            EX_MEM_RegisterRd_out.next = ID_EX_RegisterRd_in
            PC_plus_4_out.next = PC_plus_4_in

            if(EX_Flush==1):
                RegWrite_out.next = 0
                MemtoReg_out.next = 0
                Branch_out.next = 0
                MemRead_out.next = 0
                MemWrite_out.next = 0
                Jump_out.next = 0

    return latches
