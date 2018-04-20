import os
import sys
from myhdl import *

base_d = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(base_d, "python/"))

from Clock_Generator import clock_generator
from Control import Control as Py_cosim

def V_cosim(clock, wb, infile):
    ALU_v = os.path.join(base_d, "verilog/ALU.v")
    Control_v = os.path.join(base_d, "verilog/Control.v")
    Cosim_o = os.path.join(base_d, "bin/Cosim.o")
    Cosim_v = os.path.join(base_d, "MIPS_cosim.v")
    DM_v = os.path.join(base_d, "verilog/Data_Memory.v")
    EX_MEM_v = os.path.join(base_d, "verilog/EX_MEM.v")
    FU_v = os.path.join(base_d, "verilog/Forwarding_Unit.v")
    HD_v = os.path.join(base_d, "verilog/Hazard_Detection_Unit.v")
    ID_EX_v = os.path.join(base_d, "verilog/ID_EX.v")
    IF_ID_v = os.path.join(base_d, "verilog/IF_ID.v")
    IM_v = os.path.join(base_d, "verilog/Instruction_Memory.v")
    MEM_WB_v = os.path.join(base_d, "verilog/MEM_WB.v")
    PC_v = os.path.join(base_d, "verilog/PC.v")
    RF_v = os.path.join(base_d, "verilog/Register.v")
    myhdl_vpi = os.path.join(base_d, "bin/myhdl.vpi")
    cmd = "iverilog -o %s %s %s %s %s %s %s %s %s %s %s %s %s %s -Din_file %s" % \
        (Cosim_o, ALU_v, Control_v, DM_v, EX_MEM_v, FU_v, HD_v, ID_EX_v, \
        IF_ID_v, IM_v, MEM_WB_v, PC_v, RF_v, infile)
    os.system(cmd)
    return Cosimulation("vvp -m %s %s" % (myhdl_vpi, Cosim_o), clock=clock, wb=wb)


@block
def match_test(clock, dver, dpy):
  @always(clock.negedge)
  def match_t():
    if (dver != dpy):
      print("No Match: v %s, py %s" % (bin(dver), bin(dpy)))
    else:
      print("Match: v %s, py %s" % (bin(dver), bin(dpy)))
  return match_t

def run_MIPS_cosim(infile):
    clock = Signal(0)
    clock_driver = clock_generator(clock)
    dpy = Signal(intbv(val = 0, min = 0, max = 2**32))
    dv = Signal(intbv(val = 0, min = 0, max = 2**32))
    py_cosim = Py_cosim(clock, dpy)
    v_cosim  = V_cosim(clock, dv, infile)
    match_t  = match_test(clock, dv, dpy)
    sim = Simulation(instances())
    sim.run(1000)

run_MIPS_cosim(sys.argv[1])
