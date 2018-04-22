module MIPS_cosim;

reg clock;
reg [31:0] registers [31:0];

initial begin
  $from_myhdl(clock, reset);
  $to_myhdl(registers);
end

Control cont(clock, reset, registers);

endmodule
