module DM_cosim;

reg Clk, MR, MW;
reg [31:0] Addr, WD;
wire [31:0] RD;

DataMemory DM(.MR(MR), .MW(MW), .Addr(Addr), .WD(WD), .Clk(Clk), .RD(RD));

initial begin
  $from_myhdl(Clk, MR, MW, Addr, WD);
  $to_myhdl(RD);
  $dumpfile("DM_cosim.vcd");
  $dumpvars (-1, DM);
end

endmodule
