`timescale 1ns / 1ns

module CPU_tb();

	parameter tck = 10; ///< clock tick
	
	reg clk, rst;
	
	integer seed = 1;
	integer num_iter = 0 ;
	always #(tck/2) clk <= ~clk; // clocking device

	wire [31:0] regOut0,regOut1,regOut2,regOut3,regOut4,regOut5,regOut6,regOut7,
		regOut8,regOut9,regOut10,regOut11,regOut12,regOut13,regOut14,regOut15,
		regOut16,regOut17,regOut18,regOut19,regOut20,regOut21,regOut22,regOut23,
		regOut24,regOut25,regOut26,regOut27,regOut28,regOut29,regOut30,regOut31;


    cpu dut (clk, rst, regOut0, regOut1, regOut2, regOut3, regOut4, regOut5, regOut6, regOut7, regOut8,
            regOut9, regOut10, regOut11, regOut12, regOut13, regOut14, regOut15, regOut16, regOut17,
            regOut18, regOut19, regOut20, regOut21, regOut22, regOut23, regOut24, regOut25, regOut26,
            regOut27, regOut28, regOut29, regOut30, regOut31
    );

	initial begin
		$dumpfile("cpu_ah.vcd");
		$dumpvars(-1, dut);
		$monitor(
			"Rst:%h|PC_in:%h|PCWrite:%h|PC_out:%h|Instr:%h|IFID_Inst:%h|IFID_PCp4:%h",
			rst, dut.third_jr_or_second_mux_2_to_1_out, dut.PCWrite, dut.PC_out, dut.instruction_out,dut.IF_ID_instruction,dut.IF_ID_PC_plus4);
		
		clk = 0;
		rst = 0;	
		#(tck*2);
		
		rst = 1;
		#(tck*2);
		
		rst = 0;
		#(tck*2);
	end
	
	always @(posedge clk) begin
		num_iter = num_iter + 1;
		if (num_iter > 1000)
			$finish;
	end
	
endmodule