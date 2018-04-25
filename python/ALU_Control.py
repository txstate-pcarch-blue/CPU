#Takes in operation values and sends out signal to ALU
from myhdl import *

@block
def alu_control(ALUop, funct, ALUcontrol):
    #depending on the operation, tell the ALU which operation to perform
    @always(ALUop, funct)
    def control():
        if (ALUop == 0):
            ALUcontrol.next = 0 #lw, sw: add
        elif (ALUop == 1):
            ALUcontrol.next = 1 #beq: sub
        elif (ALUop == 2):
            ALUcontrol.next = 0 #addi: add
        elif (ALUop == 3):
            ALUcontrol.next = 1 #subi: add
        elif (ALUop == 4):
            if (funct == 0):
                ALUcontrol.next = 0 #add
            elif (funct == 2):
                ALUcontrol.next = 1 #sub
            elif (funct == 6):
                ALUcontrol.next = 2 #xor

    return control

@block
def JR_Control(alu_op, funct, JRControl):
    #tell the ALU to jump
    @always_comb
    def control():
        if (alu_op == 0 and funct == 8):
            JRControl = 1
        else:
            JRControl = 0

    return control
