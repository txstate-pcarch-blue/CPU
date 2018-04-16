module pc  (input [31:0] addrIn,
             input clk, reset, branch,
             output reg [31:0] addrOut);

always @(posedge clk) begin
	if(reset == 1) begin
		addrOut <= 32'b0;
	end

	else begin
		if(branch == 1) addrOut <= addrIn;
		else addrOut <= addrOut+4;

	end

	end

endmodule