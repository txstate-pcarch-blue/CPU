import os
from myhdl import Simulation, Cosimulation, Signal, traceSignals, intbv, instances
from helpers.Paths import *
from helpers.Clock_Generator import clock_generator
from helpers.Pulse_Generator import pulse_generator
from helpers.Random_Signal import random_signal
from helpers.Match_Test import match_test_report
from Data_Memory import Data_Memory as py_dm


def v_dm(clock, MR, MW, Addr, WD, RD):
    cmd = 'iverilog -o %s %s %s' % (DM_cosim_o, DM_cosim_v, DM_v)
    os.system(cmd)
    return Cosimulation("vvp -m %s %s" % (myhdl_vpi, DM_cosim_o),
                        Clk=clock, MR=MR, MW=MW, Addr=Addr, WD=WD, RD=RD)

def run_IM_cosim():
    # Initiate signals
    MAX_TIME = 1000000
    clock = Signal(0)
    MR = Signal(0, delay=10)
    MW = Signal(0, delay=10)
    address = Signal(intbv(0, 0, 2**32), delay=10)
    WD = Signal(intbv(0, 0, 2**32), delay=10)
    pyData = Signal(intbv(0, 0, 2**32))
    vData = Signal(intbv(0, 0, 2**32))

    # Build driver instances
    clock_driver = clock_generator(clock, period=20)
    addr_driver = random_signal(clock, address, seed=1)
    WD_driver = random_signal(clock, WD, seed=2)
    MR_driver = pulse_generator(clock, MR, delay=2)
    MW_driver = pulse_generator(clock, MW, delay=3)
    py_cosim = traceSignals(py_dm(clock, address, MW, MR, pyData, WD, inmem))
    v_cosim = v_dm(clock, MR, MW, address, WD, vData)
    read_test = match_test_report(clock, vData, pyData, a_name="v:", b_name="py:")

    sim = Simulation(instances())
    sim.run(MAX_TIME)

run_IM_cosim()
