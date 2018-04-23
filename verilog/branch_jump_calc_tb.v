module branch_jump_calc_tb();
	
	reg [31:0] In1_extended_imm;
	reg [31:0] In2_pc_plus_4_b;
	
	reg [31:0] In1_instruction;
	reg [31:0] In2_pc_plus_4_j;
	
	wire [31:0] BTA;
	wire [31:0] Jump_Address;
		
	branch_calculator dut (In1_extended_imm, In2_pc_plus_4_b, BTA);
	
	jump_calculator dut2 (In1_instruction, In2_pc_plus_4_j, Jump_Address);
	
	
	initial begin
		In1_extended_imm <= 32'h00000000;
		In2_pc_plus_4_b <= 32'h00000000;
		
		In1_instruction <= 32'h00000000; 
		In2_pc_plus_4_j <= 32'h00000000; 

		#1;
		$display("Branch, Inputs: %h, %h output: %h", In1_extended_imm, In2_pc_plus_4_b, BTA);
		$display("Jump, Inputs: %h, %h output: %h", In1_instruction, In2_pc_plus_4_j, Jump_Address);
		
		#1;
		//branch address result after calculation should be 0x10000008
		In1_extended_imm <= 32'h00000001;
		In2_pc_plus_4_b <= 32'h10000004;
		
		//jump address result after calc should be 0x70000008
		In1_instruction <= 32'h00000001; 
		In2_pc_plus_4_j <= 32'h70000000; 
		
		#1;
		$display("Branch, Inputs: %h, %h output: %h", In1_extended_imm, In2_pc_plus_4_b, BTA);
		$display("Jump, Inputs: %h, %h output: %h", In1_instruction, In2_pc_plus_4_j, Jump_Address);
		
		
	end	
endmodule