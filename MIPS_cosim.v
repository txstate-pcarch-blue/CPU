module MIPS_cosim;

reg clock;
reg [31:0] wb;

initial begin
  $from_myhdl(clock);
  $to_myhdl(wb);
end

Control cont(clock, wb);

endmodule
