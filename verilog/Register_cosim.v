module Registers_cosim;


reg clock, writeSignal, reset;
wire [31:0] readA, readB;
reg [31:0] write;
reg [4:0] rAddrA, rAddrB, wAddr;
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
wire [31:0] regOut16;
wire [31:0] regOut17;
wire [31:0] regOut18;
wire [31:0] regOut19;
wire [31:0] regOut20;
wire [31:0] regOut21;
wire [31:0] regOut22;
wire [31:0] regOut23;
wire [31:0] regOut24;
wire [31:0] regOut25;
wire [31:0] regOut26;
wire [31:0] regOut27;
wire [31:0] regOut28;
wire [31:0] regOut29;
wire [31:0] regOut30;
wire [31:0] regOut31;

initial begin
  $from_myhdl(write, rAddrA, rAddrB, wAddr, writeSignal, clock, reset);
  $to_myhdl(readA, readB, regOut0, regOut1, regOut2, regOut3, regOut4, regOut5, regOut6,
            regOut7, regOut8, regOut9, regOut10, regOut11, regOut12, regOut13, regOut14,
            regOut15, regOut16, regOut17, regOut18, regOut19, regOut20, regOut21, regOut22,
            regOut23, regOut24, regOut25, regOut26, regOut27, regOut28, regOut29, regOut30,
            regOut31 );
end


RegisterFile rf(
		.BusA(readA), .BusB(readB), .BusW(write), .RA(rAddrA), .RB(rAddrB), .RW(wAddr),
		.RegWr(writeSignal), .Clk(clock), .Rst(reset),
		.regOut0(regOut0), .regOut1(regOut1), .regOut2(regOut2), .regOut3(regOut3), .regOut4(regOut4),
		.regOut5(regOut5), .regOut6(regOut6), .regOut7(regOut7), .regOut8(regOut8), .regOut9(regOut9),
		.regOut10(regOut10), .regOut11(regOut11), .regOut12(regOut12), .regOut13(regOut13), .regOut14(regOut14),
		.regOut15(regOut15), .regOut16(regOut16), .regOut17(regOut17), .regOut18(regOut18), .regOut19(regOut19),
		.regOut20(regOut20), .regOut21(regOut21), .regOut22(regOut22), .regOut23(regOut23), .regOut24(regOut24),
		.regOut25(regOut25), .regOut26(regOut26), .regOut27(regOut27), .regOut28(regOut28), .regOut29(regOut29),
		.regOut30(regOut30), .regOut31(regOut31) );

endmodule
