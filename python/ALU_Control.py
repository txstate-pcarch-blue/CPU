from myhdl import *

@block
def alu_control(ALUop, funct, ALUcontrol):

    @always(ALUop, funct)
    def control():
        if (ALUop == 0):
            ALUcontrol.next = 0
        elif (ALUop == 1):
            ALUcontrol.next = 1
        elif (ALUop == 2):
            ALUcontrol.next = 0
        elif (ALUop == 3):
            ALUcontrol.next = 1
        elif (ALUop == 4):
            if (funct == 0):
                ALUcontrol.next = 0
            elif (funct == 2):
                ALUcontrol.next = 1
            elif (funct == 6):
                ALUcontrol.next = 2

    return control

@block
def JR_Control(alu_op, funct, JRControl):

    @always_comb
    def control():
        if (alu_op == 0 and funct == 8):
            JRControl = 1
        else:
            JRControl = 0

    return control
