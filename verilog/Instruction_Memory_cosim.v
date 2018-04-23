module IM_cosim;

reg clock;
reg [31:0] addr;
wire [31:0] Instr;

InstructionMemory IM(.Addr(addr), .Clk(clock), .Inst(Instr));
defparam IM.in_file = "../samples/Index_Memory_256.hex";

initial begin
  $from_myhdl(clock, addr);
  $to_myhdl(Instr);
  $dumpfile("IM_cosim.vcd");
  $dumpvars (-1, IM);
end

endmodule
