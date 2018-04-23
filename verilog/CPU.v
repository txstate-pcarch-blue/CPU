//MODULES
`include "PC.v"
`include "Instruction_Memory.v"
`include "Register.v"
`include "ALU.v"
`include "Data_Memory.v"

//CONTROL
`include "Control.v"
`include "ALU_Control.v"
`include "branch_jump_calc.v"
`include "Forwarding_Unit.v"
`include "Hazard_Detection_Unit.v"
`include "Multiplexers.v"


//PIPELINE REGISTERS
`include "IF_ID.v"
`include "ID_EX.v"
`include "EX_MEM.v"
`include "MEM_WB.v"

//CPU - five stage MIPS CPU with forwarding and hazard control
//This file drives the processor. Control wiring signals are handled here.
//Wires are associated with their respective stage 
//Multiplexers drive control decision making
//Modules receive pre-determined inputs based on mux output

module cpu (clk, rst
);

	input clk, rst;

	// wires in IF stage
	wire [31:0] PC_in;  
	wire [31:0] PC_out;
	wire [31:0] PC_plus4; 
	wire [31:0] instruction_out;
	
	assign PC_plus4 = PC_out + 4;
	assign PC_in = PC_plus4;
	
	// wires in ID stage
	wire [31:0] IF_ID_PC_plus4, IF_ID_instruction;
	wire [4:0] MEM_WB_RegisterRd;
	wire [31:0] reg_read_data_1, reg_read_data_2;
	
	wire [31:0] immi_sign_extended;
	
	// jump within ID stage
	wire [31:0] BTA, Jump_Address;
	wire [27:0] jump_base28;
	
	// control signal generation within ID stage
	wire Jump, Branch, MemRead, MemWrite, ALUSrc, RegWrite;
	wire [1:0] RegDst, MemToReg;
	wire [2:0] ALUOp;

	// Constants within the ID stage
	wire [4:0] In3_jal_ra;
	assign In3_jal_ra = 5'b11111;


	
	//mux output wires
	wire [31:0] first_alu_mux_3_to_1_out;
	wire [31:0] second_alu_mux_3_to_1_out;
	wire [31:0] third_alu_mux_2_to_1_out;
	wire [4:0] idEx_to_exMem_mux_2_to_1_out;
	wire [31:0] writeback_source_mux_3_to_1_out;
	wire [4:0] regDst_mux_3_to_1_out;
	wire [31:0] first_jump_or_branch_mux_2_to_1_out;
	wire [31:0] second_jump_or_branch_mux_2_to_1_out;
	wire [31:0] third_jump_or_branch_mux_2_to_1_out;
	wire h_RegWrite_out, h_MemWrite_out;
	
	
	// wires for lw hazard stall
	wire PCWrite;					// PC stops writing if PCWrite == 0
	wire IF_ID_Write;				// IF/ID reg stops writing if IF_ID_Write == 0
	wire ID_Flush_lwstall;
	// wires for jump/branch control hazard
	wire PCSrc;
	wire IF_Flush, ID_Flush_Branch, EX_Flush;
	
	// Register wires
	wire [31:0] regOut0,regOut1,regOut2,regOut3,regOut4,regOut5,regOut6,regOut7,
		regOut8,regOut9,regOut10,regOut11,regOut12,regOut13,regOut14,regOut15,
		regOut16,regOut17,regOut18,regOut19,regOut20,regOut21,regOut22,regOut23,
		regOut24,regOut25,regOut26,regOut27,regOut28,regOut29,regOut30,regOut31;

	assign immi_sign_extended = IF_ID_instruction[15:0];
	
	
	//*************************************
	// wires in EX stage
	//*************************************
	wire ID_EX_Jump, ID_EX_Branch, ID_EX_MemRead, ID_EX_MemWrite, ID_EX_ALUSrc, ID_EX_RegWrite;
	wire [1:0] ID_EX_RegDst, ID_EX_MemtoReg;
	wire [2:0] ID_EX_ALUOp;
	wire [31:0] ID_EX_jump_addr, ID_EX_branch_address;
	wire [31:0] ID_EX_PC_plus4, ID_EX_reg_read_data_1, ID_EX_reg_read_data_2;
	wire [31:0] ID_EX_immi_sign_extended;
	wire [4:0] ID_EX_RegisterRs, ID_EX_RegisterRt, ID_EX_RegisterRd;
	wire [4:0] EX_RegisterRd;
	wire [5:0] ID_EX_funct;
	wire [1:0] out_to_ALU;
	wire [31:0] muxA_out, muxB_out;
	wire [31:0] after_ALUSrc;
	wire [31:0] ALU_result;
	wire ALU_zero;
	wire JRControl;
	wire [31:0] after_shift;

	//*************************************
	// wires in MEM stage
	//*************************************
	wire [4:0] EX_MEM_RegisterRd;
	wire EX_MEM_Branch, EX_MEM_MemRead, EX_MEM_MemWrite, EX_MEM_Jump;
	wire [1:0] EX_MEM_MemtoReg;
	wire EX_MEM_RegWrite;
	wire [31:0] EX_MEM_jump_addr, EX_MEM_branch_addr;
	wire EX_MEM_ALU_zero;
	wire [31:0] EX_MEM_ALU_result, EX_MEM_reg_read_data_2;
	wire [31:0] D_MEM_data;  //from DM stage output
	wire Branch_taken;
	//*************************************
	// wires in WB stage
	//*************************************
	wire [31:0] reg_write_data;
	wire MEM_WB_RegWrite;
	wire [1:0] MEM_WB_MemtoReg;
	wire [31:0] MEM_WB_D_MEM_read_data, MEM_WB_D_MEM_read_addr;
	
	
	// wires for forwarding
	wire [1:0] ForwardA, ForwardB;
	
	//*************************************
	// (WORKING) IF stage: PC, IM, IF_ID_reg
	//*************************************
	pc Unit0 (
		.PC_in(PC_in), .clk(clk), .reset(rst),  .PCWrite(PCWrite), .PC_out(PC_out)
	);
	
	InstructionMemory Unit1 (
		.Addr(PC_out), .Clk(clk), .Inst(instruction_out)
	);
	defparam Unit1.in_file = "instructions.txt";
	
	IF_ID Unit3 (
		.InsIn(instruction_out), .PC_plus4_In(PC_plus4), .InsOut(IF_ID_instruction), .PC_plus4_out(IF_ID_PC_plus4), .IFID_write(IF_ID_Write), .IF_flush(IF_Flush), .clk(clk), .reset(rst)
	);
	
	//*************************************
	// ID stage: Control, Registers, branch_jump_calc, sign_extend (automatic in Verilog, //should not have to manually do this), regDst_mux_3_to_1, 
	// ID_EX_reg, hazard_detection_unit
	//
	// What works: Control, Registers
	// What is NOT verified: everything else
	//*****************************************
	Control Unit4 (
		.opcode(IF_ID_instruction[31:26]), .ALUSrc(ALUSrc), .RegDst(RegDst), .MemWrite(MemWrite), .MemRead(MemRead), .Beq(Branch), .Jump(Jump), .MemToReg(MemToReg), .RegWrite(RegWrite), .ALUOp(ALUOp)
	);
	
	regDst_mux_3_to_1 Unit5 (
		.In1_imm_destination_rt(IF_ID_instruction[20:16]), .In2_rType_rd(IF_ID_instruction[25:21]), .In3_jal_ra(In3_jal_ra), .Ctrl_RegDst(RegDst), .out(regDst_mux_3_to_1_out)
	);
	
	hazard_unit Unit25(
		.ID_EX_MemRead(ID_EX_MemRead), .ID_EX_RegRt(ID_EX_RegisterRt), .IF_ID_RegRs(IF_ID_instruction[25:21]), .IF_ID_RegRt(IF_ID_RegRt[20:16]), .Mux_Select_Stall(ID_Flush_lwstall), .PCWrite(PCWrite), .IF_ID_Write(IF_ID_Write)
	);
	
	hazard_stall_mux_2_to_1 Unit6(
	    .h_RegWrite(RegWrite), .h_MemWrite(MemWrite), .Ctrl_Mux_Select_Stall(ID_Flush_lwstall), .h_RegWrite_out(h_RegWrite_out), .h_MemWrite_out(h_MemWrite_out)
	);
	
	RegisterFile Unit7(
		.BusA(reg_read_data_1), .BusB(reg_read_data_2), .BusW(reg_write_data), .RA(IF_ID_instruction[25:21]), .RB(IF_ID_instruction[20:16]), .RW(regDst_mux_3_to_1_out), .RegWr(RegWrite), .Clk(clk), .Rst(rst),
		.regOut0(regOut0), .regOut1(regOut1), .regOut2(regOut2), .regOut3(regOut3), .regOut4(regOut4), .regOut5(regOut5), .regOut6(regOut6), .regOut7(regOut7),
		.regOut8(regOut8), .regOut9(regOut9), .regOut10(regOut10),.regOut11(regOut11),.regOut12(regOut12),.regOut13(regOut13),.regOut14(regOut14),.regOut15(regOut15),
		.regOut16(regOut16),.regOut17(regOut17),.regOut18(regOut18),.regOut19(regOut19),.regOut20(regOut20),.regOut21(regOut21),.regOut22(regOut22),.regOut23(regOut23),
		.regOut24(regOut24),.regOut25(regOut25),.regOut26(regOut26),.regOut27(regOut27),.regOut28(regOut28),.regOut29(regOut29),.regOut30(regOut30),.regOut31(regOut31)
	);
	
	
	branch_calculator Unit8(
		.In1_extended_imm(immi_sign_extended), .In2_pc_plus_4(IF_ID_PC_plus4), .BTA(BTA)
	);
	jump_calculator Unit9(
		.In1_instruction(IF_ID_instruction), .In2_pc_plus_4(IF_ID_PC_plus4), .Jump_Address(Jump_Address)
	);
	
	// Beware, there be dragons here!
	ID_EX Unit24(
		.ID_Hazard_lwstall(ID_Flush_lwstall), .ID_Hazard_Branch(ID_Flush_Branch),
		.Branch_in(Branch), .MemRead_in(MemRead), .MemWrite_in(MemWrite), .Jump_in(Jump),
		.RegWrite_in(RegWrite), 
		.ALUSrc_in(ALUSrc),
		.ALUOp_in(ALUOp), .RegDst_in(RegDst), .MemtoReg_in(MemToReg),
		 .jump_addr_in(Jump_Address), .branch_addr_in(BTA), 
		 .PC_plus4_in(IF_ID_PC_plus4),
		 .reg_read_data_1_in(reg_read_data_1), .reg_read_data_2_in(reg_read_data_2), .immi_sign_extended_in(immi_sign_extended),
		.IF_ID_RegisterRs_in(IF_ID_instruction[25:21]), .IF_ID_RegisterRt_in(IF_ID_instruction[20:16]), .IF_ID_RegisterRd_in(IF_ID_instruction[15:11]),
		.IF_ID_funct_in(IF_ID_instruction[5:0]),
		.clk(clk), .rst(rst),
		
		.RegWrite_out(ID_EX_RegWrite), 
		.Branch_out(ID_EX_Branch), .MemRead_out(ID_EX_MemRead), .MemWrite_out(ID_EX_MemWrite), .Jump_out(ID_EX_Jump),
		.ALUSrc_out(ID_EX_ALUSrc),
		.ALUOp_out(ID_EX_ALUOp), .RegDst_out(ID_EX_RegDst), .MemtoReg_out(ID_EX_MemtoReg),
		.jump_addr_out(ID_EX_jump_addr), .branch_addr_out(ID_EX_branch_address), 
		.PC_plus4_out(ID_EX_PC_plus4),
	    .reg_read_data_1_out(ID_EX_reg_read_data_1), .reg_read_data_2_out(ID_EX_reg_read_data_2), .immi_sign_extended_out(ID_EX_immi_sign_extended),
	    .ID_EX_RegisterRs_out(ID_EX_RegisterRs), .ID_EX_RegisterRt_out(ID_EX_RegisterRt), .ID_EX_RegisterRd_out(ID_EX_RegisterRd),
	    .ID_EX_funct_out(ID_EX_funct)
	);
	
	//*************************************
	// EX Stage: ALU, ALU_Control, JRControl, Forwarding_Unit, alu muxes 1,2,3, ex_to_mem_mux, EX_MEM_reg
	//*************************************
	ALUControl Unit11(.ALUcontrol(out_to_ALU), .ALUop(ID_EX_ALUOp), .funct(ID_EX_funct));
	
	JR_Control Unit12(.alu_op(ID_EX_ALUOp), .funct(ID_EX_funct), .JRControl(JRControl));
	
	ForwardingUnit Unit13(
		.ID_EX_RegRs(ID_EX_RegisterRs), .ID_EX_RegRt(ID_EX_RegisterRt), .EX_MEM_RegRd(EX_MEM_RegisterRd), .MEM_WB_RegRd(MEM_WB_RegisterRd),
		.MEM_WB_RegWrite(MEM_WB_RegWrite), .EX_MEM_RegWrite(EX_MEM_RegWrite)
	);
	
	// ALU depends on muxes and does not receive any input directly. 
	// Output of 1st mux is ALU's 1st input
	// Output of 2nd mux feeds into 3rd mux as an input
	// Output of 3rd mux is ALU's 2nd input
	first_alu_mux_3_to_1 Unit14(.In1_RegRs(ID_EX_reg_read_data_1), .In2_fwdEx(EX_MEM_reg_read_data_2), .In3_fwdMem(MEM_WB_D_MEM_read_data), .Ctrl_FwdA(ForwardA), .out(first_alu_mux_3_to_1_out));
	
	second_alu_mux_3_to_1 Unit15(.In1_RegRt(ID_EX_reg_read_data_2), .In2_fwdEx(EX_MEM_reg_read_data_2), .In3_fwdMem(MEM_WB_D_MEM_read_data), .Ctrl_FwdB(ForwardB), .out(second_alu_mux_3_to_1_out));
	
	third_alu_mux_2_to_1 Unit16(
		.In1_second_alu_mux(second_alu_mux_3_to_1_out), .In2_immediate(immi_sign_extended), .Ctrl_ALUSrc(ALUSrc), .out(third_alu_mux_2_to_1_out)
	);
	
	
	alu Unit10(
		.A(first_alu_mux_3_to_1_out), .B(third_alu_mux_2_to_1_out), .ALUControl(out_to_ALU), .clk(clk), .reset(rst), .R(ALU_result), .zero(ALU_zero)
	);

	idEx_to_exMem_mux_2_to_1 Unit17(
		.In1_rd(ID_EX_RegisterRd), .In2_rt(ID_EX_RegisterRt), .Ctrl_RegDst(ID_EX_RegDst), .out(idEx_to_exMem_mux_2_to_1_out)
	);
	
	// Beware, there be giant squid here!
	// .ID_EX_RegisterRd_in(idEx_to_exMem_mux_2_to_1) is intentional!
	EX_MEM Unit18(
		.clk(clk), .rst(rst),
		.EX_Flush(EX_Flush),
		.RegWrite_in(ID_EX_RegWrite), 
		.MemtoReg_in(ID_EX_MemtoReg),
		.Branch_in(ID_EX_Branch), .MemRead_in(ID_EX_MemRead), .MemWrite_in(ID_EX_MemWrite), .Jump_in(ID_EX_Jump),
		.jump_addr_in(ID_EX_jump_addr), .branch_addr_in(ID_EX_branch_address),
		.ALU_zero_in(ALU_zero),
		.ALU_result_in(ALU_result), .reg_read_data_2_in(second_alu_mux_3_to_1_out),
		.ID_EX_RegisterRd_in(idEx_to_exMem_mux_2_to_1_out),
		
		.RegWrite_out(EX_MEM_RegWrite), 
		.MemtoReg_out(EX_MEM_MemtoReg),
		.Branch_out(EX_MEM_Branch), .MemRead_out(EX_MEM_MemRead), .MemWrite_out(EX_MEM_MemWrite), .Jump_out(EX_MEM_Jump),
		.jump_addr_out(EX_MEM_jump_addr), .branch_addr_out(EX_MEM_branch_addr),
		.ALU_zero_out(EX_MEM_ALU_zero),
		.ALU_result_out(EX_MEM_ALU_result), .reg_read_data_2_out(EX_MEM_reg_read_data_2),
		.EX_MEM_RegisterRd_out(EX_MEM_RegisterRd)
	);
	
	//*************************************
	// MEM Stage: Data_Memory, MEM_WB_Reg, jump/branch muxes 1,2,3,
	//*************************************
	DataMemory Unit19(.MR(EX_MEM_MemRead), .MW(EX_MEM_MemWrite), .Addr(EX_MEM_ALU_result), .WD(EX_MEM_reg_read_data_2), .Clk(clk), .RD(D_MEM_data));
	
	// Beware, there be alien engineers here!
	MEM_WB Unit20(
		.RegWrite_in(EX_MEM_RegWrite), 
		.MemtoReg_in(EX_MEM_MemtoReg),
		.D_MEM_read_data_in(D_MEM_data), .D_MEM_read_addr_in(EX_MEM_ALU_result),
		.EX_MEM_RegisterRd_in(EX_MEM_RegisterRd),
		.clk(clk), .rst(rst),
        
		.D_MEM_read_data_out(MEM_WB_D_MEM_read_data), .D_MEM_read_addr_out(MEM_WB_D_MEM_read_addr),
		.MEM_WB_RegisterRd_out(MEM_WB_RegisterRd),
		.RegWrite_out(MEM_WB_RegWrite), 
		.MemtoReg_out(MEM_WB_MemtoReg)
	);
	
	//This likely won't work but intent is to create an AND gate to compare 
	//ALU zero with Control's branch signal
	wire branch_taken;
	assign branch_taken = (ALU_zero & Branch);
	
	first_jump_or_branch_mux_2_to_1 Unit21(.In1_PC_plus_4(ID_EX_PC_plus4), .In2_BTA(BTA), .Ctrl_Branch_Gate(branch_taken), .out(first_jump_or_branch_mux_2_to_1_out));
	
	second_jump_or_branch_mux_2_to_1 Unit22(
		.In1_first_mux(first_jump_or_branch_mux_2_to_1_out), .In2_jump_addr_calc(Jump_Address), .Ctrl_Jump(Jump), .out(second_jump_or_branch_mux_2_to_1_out)
	);
	
	third_jump_or_branch_mux_2_to_1 Unit23(
		.In1_second_mux(second_jump_or_branch_mux_2_to_1_out), .In2_reg_value_ra(regOut31), .JRCtrl(JRControl), .out(third_jump_or_branch_mux_2_to_1_out)
	);
	
	//*************************************
	// WB Stage: mux?
	//*************************************
	
endmodule