from myhdl import *

@block
def mem_wb(clk, rst, RegWrite_in, MemtoReg_in, D_MEM_read_data_in, D_MEM_read_addr_in,
            EX_MEM_RegisterRd_in, D_MEM_read_data_out, D_MEM_read_addr_out, MEM_WB_RegisterRd_out,
            RegWrite_out, MemtoReg_out):

            @always(clk.negedge)
            def latch():
                if(rst==1):
                    RegWrite_out.next = 0
                    MemtoReg_out.next = 0
                    D_MEM_read_data_out.next = 0
                    D_MEM_read_addr_out.next = 0
                    MEM_WB_RegisterRd_out.next = 0
                else:
                    RegWrite_out.next = RegWrite_in
                    MemtoReg_out.next = MemtoReg_in
                    D_MEM_read_data_out.next = D_MEM_read_data_in
                    D_MEM_read_addr_out.next = D_MEM_read_addr_in
                    MEM_WB_RegisterRd_out.next = EX_MEM_RegisterRd_in

            return latch
