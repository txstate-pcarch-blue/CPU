from myhdl import *

@block
def mem_wb(clk, rst, RegWrite_in, MemtoReg_in, D_MEM_read_data_in, D_MEM_read_addr_in,
            EX_MEM_RegisterRd_in, PC_plus_4_in, D_MEM_read_data_out, D_MEM_read_addr_out, MEM_WB_RegisterRd_out,
            RegWrite_out, MemtoReg_out, PC_plus_4_out):

            @always(clk.posedge)
            def latch():
                #if reset, reset signals
                if(rst==1):
                    RegWrite_out.next = 0
                    MemtoReg_out.next = 0
                    D_MEM_read_data_out.next = 0
                    D_MEM_read_addr_out.next = 0
                    MEM_WB_RegisterRd_out.next = 0
                    PC_plus_4_out.next = 0
                #if not, send signals through normally
                else:
                    RegWrite_out.next = RegWrite_in
                    MemtoReg_out.next = MemtoReg_in
                    D_MEM_read_data_out.next = D_MEM_read_data_in
                    D_MEM_read_addr_out.next = D_MEM_read_addr_in
                    MEM_WB_RegisterRd_out.next = EX_MEM_RegisterRd_in
                    PC_plus_4_out.next = PC_plus_4_in

            return latch
