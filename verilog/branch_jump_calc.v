//Sign extend 16 bit offset 
//Shift by 2 / multiply by 4. PC is already word aligned, immediate value must be aligned 
//Add resulting 32 bit address to PC + 4 to obtain BTA
//Inputs: immediate (or offset) value already sign extended to 32bits
//Outputs: BTA (32bits)
module branch_calculator(In1_extended_imm, In2_pc_plus_4, BTA);
	
	input [31:0] In1_extended_imm;
	input [31:0] In2_pc_plus_4;
	
	output reg [31:0] BTA;
	
	always @(In1_extended_imm) begin
		BTA <= (In1_extended_imm << 2) + In2_pc_plus_4;
	end
endmodule



//Shift by 2 / multiply 26 bit value by 4
//Jumping is PC-relative, concatenate first 4 bits of PC to left of jump address.
//Resulting 32 bit address is the jump value.
//Inputs: Instr[25:0] - last 26 bits of instruction
//Outputs: Jump Address 32bits
module jump_calculator(In1_instruction, In2_pc_plus_4, Jump_Address);

	input [31:0] In1_instruction;
	input [31:0] In2_pc_plus_4;
	
	output reg [31:0] Jump_Address;
	reg [27:0] temp;
	
	always @(In1_instruction) begin
		temp = In1_instruction[25:0] << 2;
		Jump_Address <= {In2_pc_plus_4[31:28],temp};
	end
endmodule
