module alu  (input [31:0] A,B,
             input [1:0] CTRL,
             input clk, reset,
             output reg [31:0] R,
			 output zero,
			 output reg ovf, branch);
		
		assign zero = (R==0); //Zero is true if output y is 0
		
        /* Decode the instruction */

        always @* begin
			if(reset == 1) begin
				R <= 16'b0;
			end

			else if(reset == 0) begin
				ovf <= 0;
				branch <= 0;
				case (CTRL)

					2'b00 /* ADD */: {ovf, R} <= A + B;
					2'b01 /* SUB */: {ovf, R} <= A - B;
					2'b10 /* XOR */: R <= A ^ B;
					2'b11 /* Branch Conditional */: begin
						if (A == B)
							branch <= 1;
						end


					//3'h2 /* XOR */:   R <= A ^ B;
					//3'h3 /* AND */:   R <= A & B;
					//3'h4 /* OR */:    R <= A | B;
					//3'h5 /* NOTA */:  R <= ~A;
					//3'h6 /* NAND */:  R <= ~(A & B);
					//3'h7 /* NOR */:   R <= ~(A | B);

					default: R <= 0;
				endcase
			end
		end
endmodule 