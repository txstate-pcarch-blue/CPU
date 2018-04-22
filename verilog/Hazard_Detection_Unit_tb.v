`timescale 1 ns / 1 ns

module tb();

    // Inputs
	reg ID_EX_MemRead, ID_EX_RegRt, IF_ID_RegRs, IF_ID_RegRt;

    // Outputs: two control signals, which determine if pipeline stalls or continues
    // Mux select which forces control signals for current EX and future MEM_WB stage to 0
    // in case of stall
	wire PCWrite, IF_ID_Write, Mux_Select_Stall;
	
	integer seed = 1;

	hazard_unit dut
	(
		.ID_EX_MemRead(ID_EX_MemRead),
		.ID_EX_RegRt(ID_EX_RegRt),
		.IF_ID_RegRs(IF_ID_RegRs),
		.IF_ID_RegRt(IF_ID_RegRt)/*, // giving error: port ``PCWrite'' is not a port of dut.
		.PCWrite(PCWrite),
		.IF_ID_Write(IF_ID_Write),
		.Mux_Select_Stall(Mux_Select_Stall)*/
	);
	  
	integer num_iter = 0;
	  
	initial begin
		$dumpfile("Hazard_Detection_Unit_ah.vcd"); 
		$dumpvars (-1, dut);
	end

	initial begin
		ID_EX_MemRead = 0;
		ID_EX_RegRt = 0;
		IF_ID_RegRs = 0;
		IF_ID_RegRt = 0;
	end
	
	always @ * begin

		ID_EX_MemRead = $random(seed);
		ID_EX_RegRt = $random(seed);
		IF_ID_RegRs = $random(seed);
		IF_ID_RegRt = $random(seed);

		#50; // delay driven (no clock)

		num_iter = num_iter + 1;

		if (num_iter > 5000)
			$finish;
	end
  
endmodule
