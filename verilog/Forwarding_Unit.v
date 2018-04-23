//forwarding unit selects the correct ALU inputs for the EX stage
//if no hazard, ALU operands come from reg file as normal
//data hazard - operand come from either EX_MEM or MEM_WB pipeline reg
//MEM/WB hazard may occur between an instruction in the EX stage and the instruction from two cycles ago 
module ForwardingUnit(
    // Inputs: the two two RegWrite signals come from the control unit
    input ID_EX_RegRs, input ID_EX_RegRt, input EX_MEM_RegRd, input EX_MEM_RegWrite,
    input MEM_WB_RegRd, input MEM_WB_RegWrite,
	
    // Outputs: multiplexers attached to the ALU
    output Mux_ForwardA, output Mux_ForwardB
);

    // EX_MEM Hazard equations
    always @(*) begin
        if (EX_MEM_RegWrite == 1 && EX_MEM_RegRd == ID_EX_RegRs) begin
            Mux_ForwardA <= 2;
        end

        if (EX_MEM_RegWrite == 1 && EX_MEM_RegRd == ID_EX_RegRt) begin
            Mux_ForwardB = 2;
        end

        // MEM_WB Hazard equations
        if(MEM_WB_RegWrite == 1 && MEM_WB_RegRd == ID_EX_RegRs &&
        (EX_MEM_RegRd != ID_EX_RegRs || EX_MEM_RegWrite == 0)) begin
            Mux_ForwardA <= 1;
        end

        if (MEM_WB_RegWrite == 1 && MEM_WB_RegRd == ID_EX_RegRt &&
        (EX_MEM_RegRd != ID_EX_RegRt || EX_MEM_RegWrite == 0)) begin
            Mux_ForwardB <= 1;
        end
    end
	
endmodule
