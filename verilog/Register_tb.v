`timescale 1 ns / 1 ns

module tb();

	parameter tck = 10; ///< clock tick
  
	reg clk, rst;
	reg [31:0]W;
	reg [3:0] RA, RB, RW;
	reg wrn;
  
	wire [31:0] A, B;
	
	integer seed = 1 ; 
	
	/*
		wire [31:0] regOut0;
		wire [31:0] regOut1;
		wire [31:0] regOut2;
		wire [31:0] regOut3;
		wire [31:0] regOut4;
		wire [31:0] regOut5;
		wire [31:0] regOut6;
		wire [31:0] regOut7;
		wire [31:0] regOut8;
		wire [31:0] regOut9;
		wire [31:0] regOut10;
		wire [31:0] regOut11;
		wire [31:0] regOut12;
		wire [31:0] regOut13;
		wire [31:0] regOut14;
		wire [31:0] regOut15;
	*/
	
	RegisterFile dut
	(
		.BusA(A), 
		.BusB(B),
		.BusW(W),
		.RA(RA),
		.RB(RB),
		.RW(RW),
		.RegWr(wrn),
		.Clk(clk),
		.Rst(rst)
		
		/*
			.regOut0(regOut0),
			.regOut1(regOut1),
			.regOut2(regOut2),
			.regOut3(regOut3),
			.regOut4(regOut4),
			.regOut5(regOut5),
			.regOut6(regOut6),
			.regOut7(regOut7),
			.regOut8(regOut8),
			.regOut9(regOut9),
			.regOut10(regOut10),
			.regOut11(regOut11),
			.regOut12(regOut12),
			.regOut13(regOut13),
			.regOut14(regOut14),
			.regOut15(regOut15)
		*/
	);
	  
	integer num_iter = 0 ;
	always #(tck/2) clk <= ~clk; // clocking device
	  
	initial begin
		$dumpfile("register_ah.vcd"); 
		$dumpvars (-1, dut);
	end
	  
	  
	initial begin
		clk = 0; rst = 0; wrn = 0;
		RA  = 4'd0;
		RB  = 4'd0;
		RW  = 4'd0;
		W = 32'd0;  
	end
	
	always @(posedge clk) begin
		RA  = $random(seed);
		RB  = $random(seed);
		RW  = $random(seed);
		W   = $random(seed);
		rst = $random(seed);
		wrn = $random(seed);
		
		++ num_iter;
	end
	
	always @(negedge clk) begin
		if (num_iter > 5000)
			$finish;
	end
  
endmodule
  
