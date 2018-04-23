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
//Changes FwdA_control to 0, 1, and then 0.

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
		In1_second_alu_mux = $random(seed);
		In2_immediate = $random(seed);
		Ctrl_ALUSrc = 1;
		#5
		$finish;
	end

endmodule

//--------------------------------------------------------------
//ID/EX to EX/MEM Multiplexor Test Bench
//Changes input registers randomly every 5 time units.
//Changes FwdA_control to 0, 1, and then 0.

module idEx_to_exMem_mux_2_to_1_tb();

parameter tck = 10; ///< clock tick

//input and output regs
reg [31:0] In1_rd, In2_rt;
reg [1:0] Ctrl_RegDst;
wire [31:0] out;

idEx_to_exMem_mux_2_to_1 dut(	

	.In1_rd(In1_rd), 
	.In2_rt(In2_rt), 
	.Ctrl_RegDst(Ctrl_RegDst),
	.out(out)
			);

integer seed = 3 ;

initial begin
		//$dumpfile("mux_tb.vcd");
		$dumpvars(-1, dut);
		$monitor("%b", out);
	end

initial begin
		Ctrl_RegDst = 0;
		#5
		Ctrl_RegDst = 0;
		In1_rd = $random(seed);
		In2_rt = $random(seed);
		#5
		In1_rd = $random(seed);
		In2_rt = $random(seed);
		Ctrl_RegDst = 1;
		#5
		In1_rd = $random(seed);
		In2_rt = $random(seed);
		Ctrl_RegDst = 0;
		#5
		In1_rd = $random(seed);
		In2_rt = $random(seed);
		Ctrl_RegDst = 1;
		#5
		$finish;
	end

endmodule

//--------------------------------------------------------------
//Writeback Source MUX Test Bench
//Changes input registers randomly every 5 time units.
//Changes FwdA_control to 0, 1, 2, and then 0.

module writeback_source_mux_3_to_1_tb();

parameter tck = 10; ///< clock tick

//input and output regs
reg [31:0] In1_ALU_Result, In2_Mem_output, In3_PC_plus_4;
reg [1:0] Ctrl_MemToReg;
wire [31:0] out;

writeback_source_mux_3_to_1 dut(	

	.In1_ALU_Result(In1_ALU_Result), 
	.In2_Mem_output(In2_Mem_output), 
	.In3_PC_plus_4(In3_PC_plus_4), 
	.Ctrl_MemToReg(Ctrl_MemToReg),
	.out(out)

			);

integer seed = 2 ;

initial begin
		//$dumpfile("mux_tb.vcd");
		$dumpvars(-1, dut);
		$monitor("%b", out);
	end

initial begin
		Ctrl_MemToReg = 0;
		#5
		Ctrl_MemToReg = 0;
		In1_ALU_Result = $random(seed);
		In2_Mem_output = $random(seed);
		In3_PC_plus_4 = $random(seed);
		#5
		Ctrl_MemToReg = 1;
		In1_ALU_Result = $random(seed);
		In2_Mem_output = $random(seed);
		In3_PC_plus_4 = $random(seed);
		#5
		Ctrl_MemToReg = 2;
		In1_ALU_Result = $random(seed);
		In2_Mem_output = $random(seed);
		In3_PC_plus_4 = $random(seed);
		#5
		Ctrl_MemToReg = 0;
		In1_ALU_Result = $random(seed);
		In2_Mem_output = $random(seed);
		In3_PC_plus_4 = $random(seed);
		#5
		$finish;
	end

endmodule

//--------------------------------------------------------------
//Write Address Determination MUX Test Bench
//Changes input registers randomly every 5 time units.
//Changes FwdA_control to 0, 1, 2, and then 0.

module regDst_mux_3_to_1_tb();

parameter tck = 10; ///< clock tick

//input and output regs
reg [31:0] In1_imm_destination_rt, In2_rType_rd, In3_jal_ra;
reg [1:0] Ctrl_RegDst;
wire [31:0] out;

regDst_mux_3_to_1 dut(	

	.In1_imm_destination_rt(In1_imm_destination_rt), 
	.In2_rType_rd(In2_rType_rd), 
	.In3_jal_ra(In3_jal_ra), 
	.Ctrl_RegDst(Ctrl_RegDst),
	.out(out)

			);

integer seed = 2 ;

initial begin
		//$dumpfile("mux_tb.vcd");
		$dumpvars(-1, dut);
		$monitor("%b", out);
	end

initial begin
		Ctrl_RegDst = 0;
		#5
		Ctrl_RegDst = 0;
		In1_imm_destination_rt = $random(seed);
		In2_rType_rd = $random(seed);
		In3_jal_ra = $random(seed);
		#5
		Ctrl_RegDst = 1;
		In1_imm_destination_rt = $random(seed);
		In2_rType_rd = $random(seed);
		In3_jal_ra = $random(seed);
		#5
		Ctrl_RegDst = 2;
		In1_imm_destination_rt = $random(seed);
		In2_rType_rd = $random(seed);
		In3_jal_ra = $random(seed);
		#5
		Ctrl_RegDst = 0;
		In1_imm_destination_rt = $random(seed);
		In2_rType_rd = $random(seed);
		In3_jal_ra = $random(seed);
		#5
		$finish;
	end

endmodule

//--------------------------------------------------------------
//1st Jump and Branch MUX Test Bench
//Changes input registers randomly every 5 time units.
//Changes FwdA_control to 0, 1, and then 0.

module first_jump_or_branch_mux_2_to_1_tb();

parameter tck = 10; ///< clock tick

//input and output regs
reg [31:0] In1_PC_plus_4, In2_BTA;
reg Ctrl_Branch_Gate;
wire [31:0] out;

first_jump_or_branch_mux_2_to_1 dut(	

	.In1_PC_plus_4(In1_PC_plus_4), 
	.In2_BTA(In2_BTA), 
	.Ctrl_Branch_Gate(Ctrl_Branch_Gate),
	.out(out)
			);

integer seed = 3 ;

initial begin
		//$dumpfile("mux_tb.vcd");
		$dumpvars(-1, dut);
		$monitor("%b", out);
	end

initial begin
		Ctrl_Branch_Gate = 0;
		#5
		Ctrl_Branch_Gate = 0;
		In1_PC_plus_4 = $random(seed);
		In2_BTA = $random(seed);
		#5
		In1_PC_plus_4 = $random(seed);
		In2_BTA = $random(seed);
		Ctrl_Branch_Gate = 1;
		#5
		In1_PC_plus_4 = $random(seed);
		In2_BTA = $random(seed);
		Ctrl_Branch_Gate = 0;
		#5
		In1_PC_plus_4 = $random(seed);
		In2_BTA = $random(seed);
		Ctrl_Branch_Gate = 1;
		#5
		$finish;
	end

endmodule

//--------------------------------------------------------------
//2nd Jump and Branch MUX Test Bench
//Changes input registers randomly every 5 time units.
//Changes FwdA_control to 0, 1, and then 0.

module second_jump_or_branch_mux_2_to_1_tb();

parameter tck = 10; ///< clock tick

//input and output regs
reg [31:0] In1_first_mux, In2_jump_addr_calc;
reg Ctrl_Jump;
wire [31:0] out;

second_jump_or_branch_mux_2_to_1 dut(	

	.In1_first_mux(In1_first_mux), 
	.In2_jump_addr_calc(In2_jump_addr_calc), 
	.Ctrl_Jump(Ctrl_Jump),
	.out(out)
			);

integer seed = 3 ;

initial begin
		//$dumpfile("mux_tb.vcd");
		$dumpvars(-1, dut);
		$monitor("%b", out);
	end

initial begin
		Ctrl_Jump = 0;
		#5
		Ctrl_Jump = 0;
		In1_first_mux = $random(seed);
		In2_jump_addr_calc = $random(seed);
		#5
		In1_first_mux = $random(seed);
		In2_jump_addr_calc = $random(seed);
		Ctrl_Jump = 1;
		#5
		In1_first_mux = $random(seed);
		In2_jump_addr_calc = $random(seed);
		Ctrl_Jump = 0;
		#5
		In1_first_mux = $random(seed);
		In2_jump_addr_calc = $random(seed);
		Ctrl_Jump = 1;
		#5
		$finish;
	end

endmodule

//--------------------------------------------------------------
//3rd Jump and Branch MUX Test Bench
//Changes input registers randomly every 5 time units.
//Changes FwdA_control to 0, 1, and then 0.

module third_jump_or_branch_mux_2_to_1_tb();

parameter tck = 10; ///< clock tick

//input and output regs
reg [31:0] In1_second_mux, In2_reg_value_ra;
reg JRCtrl;
wire [31:0] out;

third_jump_or_branch_mux_2_to_1 dut(	

	.In1_second_mux(In1_second_mux), 
	.In2_reg_value_ra(In2_reg_value_ra), 
	.JRCtrl(JRCtrl),
	.out(out)
			);

integer seed = 3 ;

initial begin
		//$dumpfile("mux_tb.vcd");
		$dumpvars(-1, dut);
		$monitor("%b", out);
	end

initial begin
		JRCtrl = 0;
		#5
		JRCtrl = 0;
		In1_second_mux = $random(seed);
		In2_reg_value_ra = $random(seed);
		#5
		In1_second_mux = $random(seed);
		In2_reg_value_ra = $random(seed);
		JRCtrl = 1;
		#5
		In1_second_mux = $random(seed);
		In2_reg_value_ra = $random(seed);
		JRCtrl = 0;
		#5
		In1_second_mux = $random(seed);
		In2_reg_value_ra = $random(seed);
		JRCtrl = 1;
		#5
		$finish;
	end

endmodule

//--------------------------------------------------------------
//Hazard Detection MUX in ID Stage
//Changes input registers randomly every 5 time units.
//Changes FwdA_control to 0, 1, and then 0.

module hazard_stall_mux_2_to_1_tb();

parameter tck = 10; ///< clock tick

//input and output regs
reg [31:0] In1_zero, In2_control_unit;
reg Ctrl_Mux_Select_Stall;
wire [31:0] out;

hazard_stall_mux_2_to_1 dut(	

	.In1_zero(In1_zero), 
	.In2_control_unit(In2_control_unit), 
	.Ctrl_Mux_Select_Stall(Ctrl_Mux_Select_Stall),
	.out(out)
			);

integer seed = 3 ;

initial begin
		//$dumpfile("mux_tb.vcd");
		$dumpvars(-1, dut);
		$monitor("%b", out);
	end

initial begin
		Ctrl_Mux_Select_Stall = 0;
		#5
		Ctrl_Mux_Select_Stall = 0;
		In1_zero = $random(seed);
		In2_control_unit = $random(seed);
		#5
		In1_zero = $random(seed);
		In2_control_unit = $random(seed);
		Ctrl_Mux_Select_Stall = 1;
		#5
		In1_zero = $random(seed);
		In2_control_unit = $random(seed);
		Ctrl_Mux_Select_Stall = 0;
		#5
		In1_zero = $random(seed);
		In2_control_unit = $random(seed);
		Ctrl_Mux_Select_Stall = 1;
		#5
		$finish;
	end

endmodule