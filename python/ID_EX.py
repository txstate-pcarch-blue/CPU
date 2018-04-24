from myhdl import *

@block
def id_ex(clk, rst, ID_Hazard_lwstall, ID_Hazard_Branch, Branch_in, MemRead_in,
            MemWrite_in, Jump_in, RegWrite_in, ALUSrc_in, ALUOp_in,
            RegDst_in, MemtoReg_in, jump_addr_in, PC_plus4_in, branch_addr_in,
            reg_read_data_1_in, reg_read_data_2_in, immi_sign_extended_in,
            IF_ID_RegisterRs_in, IF_ID_RegisterRt_in, IF_ID_RegisterRd_in,
            IF_ID_funct_in, RegWrite_out, Branch_out, MemRead_out, MemWrite_out,
            Jump_out, ALUSrc_out, ALUOp_out, RegDst_out, MemtoReg_out,
            jump_addr_out, PC_plus4_out, branch_addr_out, reg_read_data_1_out, reg_read_data_2_out,
            immi_sign_extended_out, ID_EX_RegisterRs_out, ID_EX_RegisterRt_out,
            ID_EX_RegisterRd_out, ID_EX_funct_out ):

    @always(clk.posedge)
    def latches():
        if(rst==1):
            RegWrite_out.next = 0
            MemtoReg_out.next = 0
            Branch_out.next = 0
            MemRead_out.next = 0
            MemWrite_out.next = 0
            Jump_out.next = 0
            RegDst_out.next = 0
            ALUSrc_out.next = 0
            ALUOp_out.next = 0
            jump_addr_out.next = 0
            PC_plus4_out.next = 0
            branch_addr_out.next = 0
            reg_read_data_1_out.next = 0
            reg_read_data_2_out.next = 0
            immi_sign_extended_out.next = 0
            ID_EX_RegisterRs_out.next = 0
            ID_EX_RegisterRt_out.next = 0
            ID_EX_RegisterRd_out.next = 0
            ID_EX_funct_out.next = 0
        else:
            RegWrite_out.next = RegWrite_in
            MemtoReg_out.next = MemtoReg_in
            Branch_out.next = Branch_in
            MemRead_out.next = MemRead_in
            MemWrite_out.next = MemWrite_in
            Jump_out.next = Jump_in
            RegDst_out.next = RegDst_in
            ALUSrc_out.next = ALUSrc_in
            ALUOp_out.next = ALUOp_in
            jump_addr_out.next = jump_addr_in
            PC_plus4_out.next = PC_plus4_in
            branch_addr_out.next = branch_addr_in
            reg_read_data_1_out.next = reg_read_data_1_in
            reg_read_data_2_out.next = reg_read_data_2_in
            immi_sign_extended_out.next = immi_sign_extended_in
            ID_EX_RegisterRs_out.next = IF_ID_RegisterRs_in
            ID_EX_RegisterRt_out.next = IF_ID_RegisterRt_in
            ID_EX_RegisterRd_out.next = IF_ID_RegisterRd_in
            ID_EX_funct_out.next = IF_ID_funct_in

        if(ID_Hazard_lwstall == 1 or ID_Hazard_Branch == 1):
            RegWrite_out.next = 0
            MemtoReg_out.next = 0
            Branch_out.next = 0
            MemRead_out.next = 0
            MemWrite_out.next = 0
            Jump_out.next = 0
            RegDst_out.next = 0
            ALUSrc_out.next = 0
            ALUOp_out.next = 0

    return latches
