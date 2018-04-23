module ALU_cosim;

reg clock, reset;
reg [2:0] ALUcontrol;
reg [31:0] A, B;
wire [31:0] R;
wire zero;

alu alu_inst(.A(A), .B(B), .ALUControl(ALUcontrol), .clk(clock), .reset(reset), .R(R), .zero(zero));

initial begin
  $from_myhdl(clock, reset, ALUcontrol, A, B);
  $to_myhdl(R, zero);
  $dumpfile("ALU_cosim.vcd");
  $dumpvars (-1, alu_inst);
end

endmodule
