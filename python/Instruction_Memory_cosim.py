import os
from myhdl import Simulation, Cosimulation, Signal, traceSignals, intbv, instances
from helpers.Paths import *
from helpers.Clock_Generator import clock_generator
from helpers.Pulse_Generator import pulse_generator
from helpers.Random_Signal import random_signal
from helpers.Match_Test import match_test_report
from Instruction_Memory import Instruction_Memory as py_im


def v_im(clock, pc, dout, infile):
    cmd = 'iverilog -o %s %s %s -Din_file=%s' % (IM_cosim_o, IM_cosim_v, IM_v, "../samples/Index_Memory_256.hex")
    os.system(cmd)
    return Cosimulation("vvp -m %s %s" % (myhdl_vpi, IM_cosim_o),
                        clock=clock, addr=pc, Instr=dout)

def run_IM_cosim():
    # Initiate signals
    MAX_TIME = 1000000
    infile = INDEX_256
    clock = Signal(0)
    address = Signal(intbv(0, 0, 2**32), delay=10)
    pyData = Signal(intbv(0, 0, 2**32))
    vData = Signal(intbv(0, 0, 2**32))

    # Build driver instances
    clock_driver = clock_generator(clock, period=20)
    addr_driver = random_signal(address, clock, seed=1)
    py_cosim = traceSignals(py_im(clock, address, pyData, infile))
    v_cosim = v_im(clock, address, vData, infile)
    read_test = match_test_report(clock, vData, pyData, a_name="v:", b_name="py:")

    sim = Simulation(instances())
    sim.run(MAX_TIME)

run_IM_cosim()
