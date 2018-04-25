#Control Unit
#Only opcode is input
#finct code is sent to ALU Control module
#RegDst must be 2 bit, 1 for R, 0 for lw, and 2 for jal
#MemToReg is 2 bits, 0 for R, 1 for lw, 2 for jal
from myhdl import *

@block
def control(opcode, ALUSrc, RegDst, MemWrite, MemRead, Beq, Jump, MemToReg, RegWrite, ALUOp):

    @always(opcode)
    def execute():
        #R-type opcode
        if(opcode==0):
            ALUSrc.next = 0
            RegDst.next = 1
            MemWrite.next = 0
            MemRead.next = 0
            Beq.next = 0
            Jump.next = 0
            MemToReg.next = 0
            RegWrite.next = 1
            ALUOp.next = 4
        #lw opcode
        elif(opcode==35):
            ALUSrc.next = 1
            RegDst.next = 0
            MemWrite.next = 0
            MemRead.next = 1
            Beq.next = 0
            Jump.next = 0
            MemToReg.next = 1
            RegWrite.next = 1
            ALUOp.next = 0
        #sw opcode
        elif(opcode==43):
            ALUSrc.next = 1
            MemWrite.next = 1
            MemRead.next = 0
            Beq.next = 0
            Jump.next = 0
            RegWrite.next = 0
            ALUOp.next = 0
        #beq opcode
        elif(opcode==4):
            ALUSrc.next = 1
            MemWrite.next = 0
            MemRead.next = 0
            Beq.next = 1
            Jump.next = 0
            MemToReg.next = 0
            RegWrite.next = 0
            ALUOp.next = 1
        #jump opcode
        elif(opcode==2):
            RegDst.next = 0
            MemWrite.next = 0
            MemRead.next = 0
            Beq.next = 0
            Jump.next = 1
            MemToReg.next = 0
            RegWrite.next = 0
        #jal opcode
        elif(opcode==3):
            ALUSrc.next = 0
            RegDst.next = 1
            MemWrite.next = 0
            MemRead.next = 0
            Beq.next = 0
            Jump.next = 0
            MemToReg.next = 0
            RegWrite.next = 1
            ALUOp.next = 4
        #addi opcode
        elif(opcode==8):
            ALUSrc.next = 1
            RegDst.next = 0
            MemWrite.next = 0
            MemRead.next = 0
            Beq.next = 0
            Jump.next = 0
            MemToReg.next = 0
            RegWrite.next = 1
            ALUOp.next = 2
        #subi opcode
        elif(opcode==9):
            ALUSrc.next = 1
            RegDst.next = 0
            MemWrite.next = 0
            MemRead.next = 0
            Beq.next = 0
            Jump.next = 0
            MemToReg.next = 0
            RegWrite.next = 1
            ALUOp.next = 3

    return execute
