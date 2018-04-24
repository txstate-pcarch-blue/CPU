from myhdl import *

@block
def control(opcode, ALUSrc, RegDst, MemWrite, MemRead, Beq, Jump, MemToReg, RegWrite, ALUOp):

    @always(opcode)
    def execute():
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
        elif(opcode==43):
            ALUSrc.next = 1
            MemWrite.next = 1
            MemRead.next = 0
            Beq.next = 0
            Jump.next = 0
            RegWrite.next = 0
            ALUOp.next = 0
        elif(opcode==4):
            ALUSrc.next = 1
            MemWrite.next = 0
            MemRead.next = 0
            Beq.next = 1
            Jump.next = 0
            MemToReg.next = 0
            RegWrite.next = 0
            ALUOp.next = 1
        elif(opcode==2):
            RegDst.next = 0
            MemWrite.next = 0
            MemRead.next = 0
            Beq.next = 0
            Jump.next = 1
            MemToReg.next = 0
            RegWrite.next = 0
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
