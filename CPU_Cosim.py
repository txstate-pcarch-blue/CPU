import os
import sys
from myhdl import *

base_d = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(base_d, "python/"))

from python.helpers.Clock_Generator import clock_generator
from python.helpers.Paths import *
from python.helpers.Match_Test import match_test_assert
from CPU import CPU as py_cpu


def v_cpu(clock, reset, vregisters , infile):
    cmd = "iverilog -o %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s -Din_file %s" % \
        (CPU_Cosim_o, ALU_v, ALU_control_v, bj_calc, Control_v, DM_v, EX_MEM_v, FU_v, HD_v, ID_EX_v,
         IF_ID_v, IM_v, MEM_WB_v, MUX_v, PC_v, RF_v, infile)
    os.system(cmd)
    return Cosimulation("vvp -m %s %s" % (myhdl_vpi, CPU_Cosim_o), clock=clock, registers=vregisters)


def run_MIPS_cosim(infile):
    const MAX_TIME = 1000000
    clock = Signal(0)
    clock_driver = clock_generator(clock)
    reset = Signal(0)

    # Make output register files for comparison
    pyregs = []
    vregs = []
    for i in range(0, 32):
        pyregs.append(Signal(intbv(0, 0, 2**32)))
        pyregs[i].driven = not pyregs[i].driven
        vregs.append(Signal(intbv(0, 0, 2**32)))
        vregs[i].driven = not vregs[i].driven

    # Create the simulations and run
    py_cosim = py_cpu(clock, reset, pyregs)
    v_cosim = v_cpu(clock, reset, vregs, infile)
    match_t = match_test_assert(clock, vregs, pyregs)
    sim = Simulation(clock_driver, py_cosim, v_cosim, match_t)
    sim.run(MAX_TIME)

run_MIPS_cosim(sys.argv[1])
