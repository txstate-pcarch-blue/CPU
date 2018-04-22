`timescale 1 ns / 1 ns

//1st ALU source rs TB
//Changes input registers randomly every 5 time units.
//Changes FwdA_control to 0, 1, 2, and then 0.

module first_alu_mux_3_to_1_tb();

parameter tck = 10; ///< clock tick

//input and output regs
reg [31:0] In1_RegRs, In2_fwdEx, In3_fwdMem;
reg [1:0] Ctrl_FwdA;
wire [31:0] out;

first_alu_mux_3_to_1 dut(	

	.In1_RegRs(In1_RegRs), 
	.In2_fwdEx(In2_fwdEx), 
	.In3_fwdMem(In3_fwdMem), 
	.Ctrl_FwdA(Ctrl_FwdA),
	.out(out)

			);

integer seed = 1 ;

initial begin
		$dumpfile("mux_tb.vcd");
		$dumpvars(-1, dut);
		$monitor("%b", out);
	end

initial begin
		Ctrl_FwdA = 0;
		#5
		Ctrl_FwdA = 0;
		In1_RegRs = $random(seed);
		In2_fwdEx = $random(seed);
		In3_fwdMem = $random(seed);
		#5
		In1_RegRs = $random(seed);
		In2_fwdEx = $random(seed);
		In3_fwdMem = $random(seed);
		Ctrl_FwdA = 1;
		#5
		In1_RegRs = $random(seed);
		In2_fwdEx = $random(seed);
		In3_fwdMem = $random(seed);
		Ctrl_FwdA = 2;
		#5
		In1_RegRs = $random(seed);
		In2_fwdEx = $random(seed);
		In3_fwdMem = $random(seed);
		Ctrl_FwdA = 0;
		#5
		$finish;
	end

endmodule

//--------------------------------------------------------------
//2nd ALU source rt test bench
//Changes input registers randomly every 5 time units.
//Changes FwdA_control to 0, 1, 2, and then 0.

module second_alu_mux_3_to_1_tb();

parameter tck = 10; ///< clock tick

//input and output regs
reg [31:0] In1_RegRt, In2_fwdEx, In3_fwdMem;
reg [1:0] Ctrl_FwdB;
wire [31:0] out;

second_alu_mux_3_to_1 dut(	

	.In1_RegRt(In1_RegRt), 
	.In2_fwdEx(In2_fwdEx), 
	.In3_fwdMem(In3_fwdMem), 
	.Ctrl_FwdB(Ctrl_FwdB),
	.out(out)

			);

integer seed = 2 ;

initial begin
		//$dumpfile("mux_tb.vcd");
		$dumpvars(-1, dut);
		$monitor("%b", out);
	end

initial begin
		Ctrl_FwdB = 0;
		#5
		Ctrl_FwdB = 0;
		In1_RegRt = $random(seed);
		In2_fwdEx = $random(seed);
		In3_fwdMem = $random(seed);
		#5
		In1_RegRt = $random(seed);
		In2_fwdEx = $random(seed);
		In3_fwdMem = $random(seed);
		Ctrl_FwdB = 1;
		#5
		In1_RegRt = $random(seed);
		In2_fwdEx = $random(seed);
		In3_fwdMem = $random(seed);
		Ctrl_FwdB = 2;
		#5
		In1_RegRt = $random(seed);
		In2_fwdEx = $random(seed);
		In3_fwdMem = $random(seed);
		Ctrl_FwdB = 0;
		#5
		$finish;
	end

endmodule


//--------------------------------------------------------------
//3rd ALU for source
//Changes input registers randomly every 5 time units.
//Changes FwdA_control to 0, 1, 2, and then 0.

module third_alu_mux_2_to_1_tb();

parameter tck = 10; ///< clock tick

//input and output regs
reg [31:0] In1_second_alu_mux, In2_immediate;
reg Ctrl_ALUSrc;
wire [31:0] out;

third_alu_mux_2_to_1 dut(	

	.In1_second_alu_mux(In1_second_alu_mux), 
	.In2_immediate(In2_immediate), 
	.Ctrl_ALUSrc(Ctrl_ALUSrc),
	.out(out)
			);

integer seed = 3 ;

initial begin
		//$dumpfile("mux_tb.vcd");
		$dumpvars(-1, dut);
		$monitor("%b", out);
	end

initial begin
		Ctrl_ALUSrc = 0;
		#5
		Ctrl_ALUSrc = 0;
		In1_second_alu_mux = $random(seed);
		In2_immediate = $random(seed);
		#5
		In1_second_alu_mux = $random(seed);
		In2_immediate = $random(seed);
		Ctrl_ALUSrc = 1;
		#5
		In1_second_alu_mux = $random(seed);
		In2_immediate = $random(seed);
		Ctrl_ALUSrc = 0;
		#5
		$finish;
	end

endmodule
