from myhdl import *

@block
def Control(opcode, ALUSrc, RegDst, MemWrite, MemRead, Beq, Jump, MemToReg, RegWrite, ALUOp):

    @always(*)
    def control():
        if(opcode==o):

        elif(opcode==35):

        elif(opcode==43):

        elif(opcode==4):

        elif(opcode==2):

        elif(opcode==3):

        elif(opcode==8):

        elif(opcode==9):


    return control
