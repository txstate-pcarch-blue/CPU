module alu  (input [15:0] A,B,
             input [2:0] CTRL,
             input clk, reset,
             output reg [15:0] R,
			 output zero);
		
		assign zero = (R==0); //Zero is true if output y is 0
        /* Decode the instruction */
        always @(posedge clk) begin
			if(reset == 1) begin
				R <= 16'b0;
			end
			else if(reset == 0) begin
				case (CTRL)
					3'h1 /* ADD */:   R <= A + B;
					3'h2 /* XOR */:   R <= A ^ B;
					3'h3 /* AND */:   R <= A & B;
					3'h4 /* OR */:    R <= A | B;
					3'h5 /* NOTA */:  R <= ~A;
					3'h6 /* NAND */:  R <= ~(A & B);
					3'h7 /* NOR */:   R <= ~(A | B);
					default: R <= 0;
				endcase
			end
		end
endmodule //alu
