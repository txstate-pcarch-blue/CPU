module RegisterFile(BusA, BusB, BusW, RA, RB, RW, RegWr, Clk, Rst
/*
regOut0,regOut1,regOut2,regOut3,regOut4,regOut5,regOut6,regOut7,regOut8,
regOut9,regOut10,regOut11,regOut12,regOut13,regOut14,regOut15
*/
);
	output reg [31:0] BusA, BusB;  //data to read
	input [31:0] BusW;  //data to write
	input [3:0] RA, RB, RW;  //read addr A, read addr B, write addr
	input RegWr;  //write ctrl
	input Clk, Rst;
	
	
	
	reg [31:0] registers [15:0];
	
	/* 
	* FOR DEBUG registers to view on GTKWave
	* Uncomment as needed
	*/
	/*
		output [31:0] regOut0;
		output [31:0] regOut1;
		output [31:0] regOut2;
		output [31:0] regOut3;
		output [31:0] regOut4;
		output [31:0] regOut5;
		output [31:0] regOut6;
		output [31:0] regOut7;
		output [31:0] regOut8;
		output [31:0] regOut9;
		output [31:0] regOut10;
		output [31:0] regOut11;
		output [31:0] regOut12;
		output [31:0] regOut13;
		output [31:0] regOut14;
		output [31:0] regOut15;
	
		assign regOut0 = registers[0];
		assign regOut1 = registers[1];
		assign regOut2 = registers[2];
		assign regOut3 = registers[3];
		assign regOut4 = registers[4];
		assign regOut5 = registers[5];
		assign regOut6 = registers[6];
		assign regOut7 = registers[7];
		assign regOut8 = registers[8];
		assign regOut9 = registers[9];
		assign regOut10 = registers[10];
		assign regOut11 = registers[11];
		assign regOut12 = registers[12];
		assign regOut13 = registers[13];
		assign regOut14 = registers[14];
		assign regOut15 = registers[15];
	*/
	
	
	integer i, j;
	
	initial begin 
		for(j = 0; j < 16; j = j + 1) begin
				registers[j] <= 0;
		end
	end
	
	always begin
		@(posedge Clk) begin
			if (RegWr)
				registers[RW] <= BusW;
			else if (Rst) begin
				for(i = 0; i < 16; i = i + 1) 
					registers[i] <= 0;
			end
		end
		
		@(negedge Clk) begin
			BusA <= registers[RA];
			BusB <= registers[RB];
		end
	end
	
endmodule