module MIPS_cosim;

reg clock, reset;
wire [31:0] regOut0,regOut1,regOut2,regOut3,regOut4,regOut5,regOut6,regOut7,
    regOut8,regOut9,regOut10,regOut11,regOut12,regOut13,regOut14,regOut15,
    regOut16,regOut17,regOut18,regOut19,regOut20,regOut21,regOut22,regOut23,
    regOut24,regOut25,regOut26,regOut27,regOut28,regOut29,regOut30,regOut31
;

initial begin
    $from_myhdl(clock, reset);
    $to_myhdl(regOut0,regOut1,regOut2,regOut3,regOut4,regOut5,regOut6,regOut7,
            regOut8,regOut9,regOut10,regOut11,regOut12,regOut13,regOut14,regOut15,
            regOut16,regOut17,regOut18,regOut19,regOut20,regOut21,regOut22,regOut23,
            regOut24,regOut25,regOut26,regOut27,regOut28,regOut29,regOut30,regOut31
    );
end

cpu dut (clock, reset, regOut0, regOut1, regOut2, regOut3, regOut4, regOut5, regOut6, regOut7, regOut8,
        regOut9, regOut10, regOut11, regOut12, regOut13, regOut14, regOut15, regOut16, regOut17,
        regOut18, regOut19, regOut20, regOut21, regOut22, regOut23, regOut24, regOut25, regOut26,
        regOut27, regOut28, regOut29, regOut30, regOut31
);

initial begin
	$dumpfile("CPU_v.vcd");
	$dumpvars(-1, dut);
end

defparam dut.in_file = "instructions.txt";

endmodule
