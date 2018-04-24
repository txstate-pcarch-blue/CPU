`timescale 1 ns / 1 ns

module ForwardingUnit_tb();

parameter tck = 10; ///< clock tick

//input and output regs
reg [4:0] ID_EX_RegRs, ID_EX_RegRt, EX_MEM_RegRd, MEM_WB_RegRd;
reg MEM_WB_RegWrite, EX_MEM_RegWrite;
wire [1:0] Mux_ForwardA, Mux_ForwardB;

ForwardingUnit dut(	

	.ID_EX_RegRs(ID_EX_RegRs),
	.ID_EX_RegRt(ID_EX_RegRt),
	.EX_MEM_RegRd(EX_MEM_RegRd),
	.EX_MEM_RegWrite(EX_MEM_RegWrite),
	.MEM_WB_RegWrite(MEM_WB_RegWrite),
	.MEM_WB_RegRd(MEM_WB_RegRd),
	.Mux_ForwardA(Mux_ForwardA),
	.Mux_ForwardB(Mux_ForwardB)

			);

integer seed = 1;

initial begin
		$dumpfile("forward_tb.vcd");
		$dumpvars(-1, dut);
		$monitor("%b", Mux_ForwardA);
	end

initial begin
	
	ID_EX_RegRs = 5'h0;
	ID_EX_RegRt = 5'h0;
	EX_MEM_RegRd = 5'h0;
	MEM_WB_RegRd = 5'h0;
	MEM_WB_RegWrite = 0;
	EX_MEM_RegWrite = 0;
	#5
		//Four different states:
		// 1.) EX_MEM_RegRd = ID_EX_RegRs; EX_MEM Write = 1
		// 2.) EX_MEM_RegRd = ID_EX_RegRt; EX_MEM Write = 1
		// 3.) MEM_WB_RegRd = ID_EX_RegRs, MEM_WB Write = 1, 
		//	EX_MEM_RegRd != ID EX RegRs; 
		// 4.) MEM_WB_RegRd = ID_EX_RegRt; MEM_WB Write = 1,
		//	EX_MEM_RegRd != ID EX RegRt;

		//State #1
		ID_EX_RegRs = 5'b11111;
		ID_EX_RegRt = 5'b0;
		EX_MEM_RegRd = 5'b11111;
		MEM_WB_RegRd = 5'b0;
		MEM_WB_RegWrite = 0;
		EX_MEM_RegWrite = 1;
		#5

		//State #2
		ID_EX_RegRs = 5'b0;
		ID_EX_RegRt = 5'b10101;
		EX_MEM_RegRd = 5'b10101;
		MEM_WB_RegRd = 5'b0;
		MEM_WB_RegWrite = 0;
		EX_MEM_RegWrite = 1;
		#5

		//State #3
		ID_EX_RegRs = 5'b00011;
		ID_EX_RegRt = 5'b0;
		EX_MEM_RegRd = 5'b0;
		MEM_WB_RegRd = 5'b00011;
		MEM_WB_RegWrite = 1;
		EX_MEM_RegWrite = 0;
		#5

		//State #4
		ID_EX_RegRs = 5'b0;
		ID_EX_RegRt = 5'b10000;
		EX_MEM_RegRd = 5'b0;
		MEM_WB_RegRd = 5'b10000;
		MEM_WB_RegWrite = 1;
		EX_MEM_RegWrite = 0;
		#5

		$finish;
	end

endmodule