//MODULES
`include "PC.v"
`include "Instruction_Memory.v"

//CONTROL

//PIPELINE REGISTERS
`include "IF_ID.v"


//CPU - five stage MIPS CPU with forwarding and hazard control
//This file drives the processor. Control wiring signals are handled here.
//Wires are associated with their respective stage 
//Multiplexers drive control decision making
//Modules receive pre-determined inputs based on mux output

module cpu (clk, rst);

	input clk, rst;

	// wires in IF stage
	wire [31:0] PC_in;  
	wire [31:0] PC_out;
	wire [31:0] PC_plus4; 
	wire [31:0] instruction_out;
	
	assign PC_plus4 = PC_out + 4;
	assign PC_in = PC_plus4;
	
	// wires in ID stage
	wire [31:0] IF_ID_PC_plus4;
	wire [31:0]	IF_ID_instruction;
	// wires for lw hazard stall
	wire PCWrite;					// PC stops writing if PCWrite == 0
	wire IF_ID_Write;				// IF/ID reg stops writing if IF_ID_Write == 0
	wire ID_Flush_lwstall;
	// wires for jump/branch control hazard
	wire PCSrc;
	wire IF_Flush, ID_Flush_Branch, EX_Flush;
	
	assign PCWrite = 1;
	assign IF_ID_Write = 1;
	
	// wires in EX stage
	
		
	// IF stage: PC, IM, IF_ID_reg
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
	
	// ID stage: Control, Registers, branch_jump_calc, sign_extend, regDst_mux_3_to_1
	
	
	
	
	
endmodule