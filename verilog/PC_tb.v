// PC Test Bench
// Branches to address "cafef00c" when counter = 11
// Else, PC = PC + 4

`timescale 1 ns / 1 ns

module pc_tb();

	parameter tck = 10; ///< clock tick

	reg [31:0] PC_in ;
	reg clk, reset, PCWrite ;
	wire [31:0] PC_out ;


	pc dut(		.PC_in(PC_in),
				.clk(clk),
				.reset(reset),
				.PCWrite(PCWrite),
				.PC_out(PC_out)
			);
			
	integer num_iter = 0 ;
	integer seed = 1 ;
	always #(tck/2) clk <= ~clk; // clocking device

	initial begin
		$dumpfile("pc_ah.vcd");
		$dumpvars(-1, dut);
		$monitor("%b", PC_out);
	end
							
	//Initialise registers

	initial begin
		clk = 0 ; 
		reset = 1 ;
		PC_in = 0 ;
		#(tck);
		reset = 0 ;
	end
	
	always @(posedge clk) begin

		if (num_iter == 11) begin
			PCWrite <= 0 ;
		end

		else begin
			PCWrite <= 1 ;
			PC_in <= $random(seed);
		end

		num_iter = num_iter+1 ;
		if (num_iter > 999) $finish;
	end


endmodule
