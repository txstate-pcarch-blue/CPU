// 32-bit PC
// data input width: 1 32-bit value (branch addr, PC+4, or jump addr)
// data output width: 1 32-bit addr
// control: 1-bit: branch or not branch

// Prevents CPU from loading inputs more than once
`define loaded

module pc  (
	input [31:0] PC_in,
    input clk, reset, PCWrite,
    
	output reg [31:0] PC_out
);

	always @(posedge clk) begin
		
		if(reset==1'b1)
			PC_out <= 0;
		else if(PCWrite)
			PC_out <= PC_in;
	end

endmodule