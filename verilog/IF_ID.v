module IF_ID(InsIn, PC_plus4_In, InsOut, PC_plus4_out, IFID_write, IF_flush, clk, reset);

output reg [31:0] InsOut, PC_plus4_out;
input [31:0] InsIn, PC_plus4_In;
input clk, reset;
input IFID_write, IF_flush;

always@(negedge clk)
    begin

      if(reset == 1) begin
        InsOut <= 32'b0;
        PC_plus4_out <= 32'b0;
      end

      else begin
        if(IFID_write == 1) begin
        	InsOut <= InsIn;
        	PC_plus4_out <= PC_plus4_In;
        end

        if(IF_flush == 1) begin
        	InsOut <= 32'b0;
        	PC_plus4_out <= 32'b0;
        end
      end
    end

endmodule