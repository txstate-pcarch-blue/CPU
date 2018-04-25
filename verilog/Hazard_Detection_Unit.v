// We detect lw hazard b/w current instruction in ID stage and previous instruction in EX stage
// Hazard occurs if prev instr. is lw
module hazard_unit(ID_EX_MemRead, ID_EX_RegRt, IF_ID_RegRs, IF_ID_RegRt, Mux_Select_Stall, PCWrite, IF_ID_Write);

    // Inputs
    input ID_EX_MemRead;
    input [4:0] ID_EX_RegRt, IF_ID_RegRs, IF_ID_RegRt;

    // Outputs: two control signals, which determine if pipeline stalls or continues
    // Mux select which forces control signals for current EX and future MEM_WB stage to 0
    // in case of stall
    output reg PCWrite, IF_ID_Write, Mux_Select_Stall;

    always @( ID_EX_MemRead, ID_EX_RegRt, IF_ID_RegRs, IF_ID_RegRt ) begin
        if (ID_EX_MemRead == 1 && ((ID_EX_RegRt == IF_ID_RegRs) || (ID_EX_RegRt == IF_ID_RegRt))) begin
            Mux_Select_Stall <= 1; PCWrite <= 0; IF_ID_Write <= 0;
        end 
		else begin
			Mux_Select_Stall <= 0; PCWrite <= 1; IF_ID_Write <= 1;
		end
    end

endmodule

//flush IF/ID, ID/EX and EX/MEM if branch OR jump is determined viable at MEM stag
module branch_or_jump_taken_flush(EX_MEM_branch_out_in, EX_MEM_jump_out_in, EX_MEM_ALU_Zero_out_in, IF_Flush, ID_Flush_Branch, EX_Flush, branch_or_jump_taken);

	input EX_MEM_branch_out_in, EX_MEM_jump_out_in, EX_MEM_ALU_Zero_out_in;
	output reg IF_Flush, ID_Flush_Branch, EX_Flush, branch_or_jump_taken;

	always @( EX_MEM_branch_out_in, EX_MEM_jump_out_in, EX_MEM_ALU_Zero_out_in ) begin
		if (((EX_MEM_ALU_Zero_out_in == 1) && (EX_MEM_branch_out_in == 1)) || (EX_MEM_jump_out_in == 1)) begin 
			IF_Flush <=1 ; ID_Flush_Branch <=1 ; EX_Flush <=1 ; branch_or_jump_taken <= 1;
		end
		else begin 
			IF_Flush <= 0; ID_Flush_Branch <= 0; EX_Flush <= 0; branch_or_jump_taken <= 0;
		end
	end
endmodule