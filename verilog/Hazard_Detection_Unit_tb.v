`timescale 1ns /  1ns

module tb();

    // Inputs
	reg ID_EX_MemRead;
	reg [4:0] ID_EX_RegRt, IF_ID_RegRs, IF_ID_RegRt;

	parameter tck = 10; ///< clock tick
	reg clk;
	always #(tck/2) clk <= ~clk; // clocking device

    // Outputs: two control signals, which determine if pipeline stalls or continues
    // Mux select which forces control signals for current EX and future MEM_WB stage to 0
    // in case of stall
	wire PCWrite, IF_ID_Write, Mux_Select_Stall;
	
	integer seed = 1;

	hazard_unit dut (
		ID_EX_MemRead,
		ID_EX_RegRt,
		IF_ID_RegRs,
		IF_ID_RegRt,
		Mux_Select_Stall,
		PCWrite,
		IF_ID_Write
	);
	  
	integer num_iter = 0;
	  
	initial begin
		$dumpfile("Hazard_Detection_Unit_ah.vcd"); 
		$dumpvars (-1, dut);
	end

	initial begin
		clk = 0;
		ID_EX_MemRead = 0;
		ID_EX_RegRt = 0;
		IF_ID_RegRs = 0;
		IF_ID_RegRt = 0;
	end

	always @(posedge clk) begin
		num_iter = num_iter + 1;
	end
	
	always @ * begin

		ID_EX_MemRead <= $random(seed);
		ID_EX_RegRt <= $random(seed);
		IF_ID_RegRs <= $random(seed);
		IF_ID_RegRt <= $random(seed);

		#5; // delay makes results more readable

		if (num_iter > 5000)
			$finish;
	end
  
endmodule
