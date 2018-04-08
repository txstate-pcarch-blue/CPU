`timescale 1 ns / 1 ns

module alu_tb();

	parameter tck = 10; ///< clock tick

	reg [31:0] a, b ;
	reg clk , reset ;
	reg [1:0] ctrl  ;
	wire [31:0] r ;
	wire zero ;
	wire ovf ;


	alu dut(	.A(a), 
				.B(b), 
				.clk(clk), 
				.CTRL(ctrl), 
				.reset(reset), 
				.R(r), 
				.zero(zero),
				.ovf(ovf) 
			);
			
	integer num_iter = 0 ;
	integer seed = 1 ;
	always #(tck/2) clk <= ~clk; // clocking device

	initial begin
		$dumpfile("alu_ah.vcd");
		$dumpvars(-1, dut);
		$monitor("%b", r);
	end
							
	//Initialise registers 
	initial begin
		clk = 0; 
		reset = 0;
		a = 0 ;
		b = 0 ;
	end
	
	always @(posedge clk) begin
		a = $random(seed) ;
		b = $random(seed) ;
		ctrl = $random(seed) ;
		++ num_iter ;
		if (num_iter > 99999) $finish;

	end

endmodule
